from .backends import Backend, Result
from .circuits import Circuit

from .virtual_provider import VirtualProvider
from .translator import Translator

from ..utils.utils import ThreadWithReturnValue as Thread

from typing import Any

class Dispatch:
    
    def __init__(self, tasks: list[tuple[Backend, Circuit, int]] = [], metadata: dict[str, Any] = {}) -> None:
        self._tasks : dict[Backend, list[tuple[Circuit, int]]] = {}
        self._metadata = metadata
        for backend,circuit,shots in tasks:
            self.add_task(backend=backend, circuit=circuit, shots=shots)
            
    def add_task(self, backend: Backend, circuit: Circuit, shots: int) -> None:
        if backend not in self._tasks:
            self._tasks[backend] = []
        self._tasks[backend].append((circuit, shots))
        
    def get_tasks(self) -> dict[Backend, list[tuple[Circuit, int]]]:
        return self._tasks.copy()
    
    def get_task(self, backend: Backend) -> list[tuple[Circuit, int]]:
        return self._tasks[backend]
    
    def get_metadata(self) -> dict[str, Any]:
        return self._metadata.copy()
    
    def get_backends(self) -> list[Backend]:
        return list(self._tasks.keys())
    
    def get_total_shots(self) -> int:
        shots = 0
        for backend in self._tasks:
            for _,s in self._tasks[backend]:
                shots += s
        return shots
    
    def to_dict(self) -> dict[str, dict[str, list[tuple[Circuit, int]]]]:
        dispatch : dict[str, dict[str, list[tuple[Circuit, int]]]] = {}
        for backend in self._tasks:
            provider = backend.provider().name()
            if provider not in dispatch:
                dispatch[provider] = {}
            if backend.name() not in dispatch[provider]:
                dispatch[provider][backend.name()] = []
            for circuit,shots in self._tasks[backend]:
                dispatch[provider][backend.name()].append((circuit, shots))
        return dispatch
    
    def __add__(self, other: 'Dispatch') -> 'Dispatch':
        d = Dispatch()
        for backend in self._tasks:
            for circuit,shots in self._tasks[backend]:
                d.add_task(backend=backend, circuit=circuit, shots=shots)
        for backend in other._tasks:
            for circuit,shots in other._tasks[backend]:
                d.add_task(backend=backend, circuit=circuit, shots=shots)
        return d
    
    def __str__(self) -> str:
        return str(self.to_dict())
    
    def __repr__(self) -> str:
        return self.__str__()

class Dispatcher:
    
    def __init__(self, virtual_provider: VirtualProvider, translator: Translator = Translator()):
        self._translator = translator
        self._virtual_provider = virtual_provider
        
    def run(self, dispatch: Dispatch, asynchronous: bool = False) -> list[Result]:
        threads = []
        for backend in dispatch.get_tasks():
            cs : list[Circuit] = []
            shots : list[int] = []
            for circuit,s in dispatch.get_task(backend):
                cs.append(circuit)
                shots.append(s)
            threads.append(Thread(target=backend.run, args=(cs, shots, asynchronous)))
            threads[-1].start()
                
        results = []
        for thread in threads:
            if thread is not None and isinstance(thread, Thread):
                res = thread.join()
                if res is not None and isinstance(res, Result):
                    results.append(res)
                elif res is not None and isinstance(res, list):
                    results.extend(res)
                    
        return results
                
    def results_ready(self, results: list[Result]) -> bool:
        for result in results:
            if not result.completed():
                return False
        return True
    
    def get_results(self, results: list[Result]) -> list[Result]:
        for result in results:
            if not result.completed():
                result.update()
        return results   
        
        
    def from_dict(self, dispatch: dict[str, dict[str, list[tuple[Circuit, int]]]], metadata: dict[str, Any] = {}) -> Dispatch:
        tasks = []
        for provider in dispatch:
            for backend in dispatch[provider]:
                for circuit,shots in dispatch[provider][backend]:
                    tasks.append((self._virtual_provider.get_backend(provider, backend), circuit, shots))
        return Dispatch(tasks=tasks, metadata=metadata)