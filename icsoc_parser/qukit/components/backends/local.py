from pytket.backends.backend import Backend as TK_Backend
from pytket.backends.status import StatusEnum

from qiskit_aer.noise import NoiseModel

from . import Provider, Backend, BackendInfo, Result
from ..circuits import Circuit
from ..translator import Translator

from pytket.extensions.qiskit.backends.aer import AerStateBackend as _AerStateBackend
from pytket.extensions.qiskit.backends import AerBackend as _AerBackend

from typing import Optional

class AerBackend(Backend):
    """Aer backend."""
    
    def __init__(self, name: str, provider: 'Local', noise_model : Optional[NoiseModel] = None, instance_name: str | None = None) -> None:
        """Initialize an IBMQ backend."""
        super().__init__(name, provider, instance_name)
        self._backend = _AerBackend(noise_model=noise_model)
        self._info = BackendInfo()
    
    def run(self, circuits: Circuit | list[Circuit], shots: int | list[int] = 1, asynchronous: bool = False) -> Result | list[Result]:
        """Run the circuits on the backend."""
        translator = Translator()
        
        if not isinstance(circuits, list):
            circuits = [circuits]
            
        _circuits = []
            
        for circuit in circuits:
            if not isinstance(circuit, Circuit):
                circuit = Circuit(circuit)
            _circuits.append(circuit)
            
        circuits = _circuits
        
        cs = [translator.translate(c, "pytket").get() for c in circuits]
        cs = [self._backend.get_compiled_circuit(c, optimisation_level=0) for c in cs]
        
        for i,c in enumerate(cs):
            if not self.is_valid(c):
                raise ValueError(f"Circuit {i} not valid for backend {self._name}")
            
        res = []
        if type(shots) is int:
            shots_ls: list[int] = [shots for _ in range(len(circuits))]
        elif type(shots) is list:
            shots_ls = shots
        else:
            raise ValueError("Invalid shots argument.")

        if not asynchronous:
            counts = [dict(result.get_counts()) for result in self._backend.run_circuits(cs, n_shots=shots)]
                
            for i,circ in enumerate(circuits):
                c = {}
                for k,v in counts[i].items():
                    k = tuple(str(i) for i in k) # type: ignore
                    c["".join(k)] = int(v) # type: ignore
                r = Result(backend=self, circuit=circ, shots=shots_ls[i], data=c, completed=True)
                res.append(r)
        else:
            handlers = self._backend.process_circuits(cs, n_shots=shots)
            for i,circ in enumerate(circuits):
                r = Result(backend=self, circuit=circ, shots=shots_ls[i], data=handlers[i], completed=False)
                res.append(r)
                
        if len(res) == 1:
            return res[0]
        else:
            return res
    
    def is_valid(self, circuit: Circuit) -> bool:
        """Check if the circuit is valid for the backend."""
        
        if not isinstance(circuit, Circuit):
            circuit = Circuit(circuit)
        
        c = (Translator().translate(circuit, "pytket")).get()
        return bool(self._backend.valid_circuit(c))
    
    def is_ready(self, result: Result) -> bool:
        return self._backend.circuit_status(result._data).status == StatusEnum.COMPLETED
    
    def get_result(self, result: Result) -> Result:
        """Return the result of a circuit."""
        
        if result.backend() != self:
            raise ValueError("Result not from this backend.")
        
        if not self.is_ready(result):
            raise ValueError("Result is not ready.")
        counts = dict(self._backend.get_result(result._data).get_counts())
        c = {}
        for k,v in counts.items():
            k = tuple(str(i) for i in k) # type: ignore
            c["".join(k)] = int(v) # type: ignore
        return Result(backend=self, circuit=result.circuit(), shots=result.shots(), data=c, completed=True)
    
    def noisy(self) -> bool:
        """Return True if the backend is noisy."""
        return self._backend._noise_model is not None
    
    def noise_model(self) -> NoiseModel:
        """Return the noise model of the backend."""
        return self._backend._noise_model
    
    def info(self) -> BackendInfo:
        """Return information about the backend."""
        return self._info
    
    def to_tk(self) -> TK_Backend:
        return self._backend
    
    def __str__(self) -> str:
        """Return a string representation of the backend."""
        return f"{self.__class__.__name__}(name={self._name}, provider={self._provider}, noise_model={self.noisy()})"

class AerStateBackend(Backend):
    """AerState backend."""
    
    def __init__(self, name: str, provider: 'Local', instance_name: str | None = None) -> None:
        """Initialize an Aer State backend."""
        super().__init__(name, provider, instance_name)
        self._backend = _AerStateBackend()
        self._info = BackendInfo()
    
    def run(self, circuits: Circuit | list[Circuit], shots: int | list[int] = 1, asynchronous: bool = False) -> Result | list[Result]:
        """Run the circuits on the backend."""
        translator = Translator()
        
        if not isinstance(circuits, list):
            circuits = [circuits]
            
        _circuits = []
            
        for circuit in circuits:
            if not isinstance(circuit, Circuit):
                circuit = Circuit(circuit)
            _circuits.append(circuit)
            
        circuits = _circuits
        
        cs = [translator.translate(c, "pytket").get() for c in circuits]
        cs = [self._backend.get_compiled_circuit(c, optimisation_level=0) for c in cs]
        
        for i,c in enumerate(cs):
            if not self.is_valid(c):
                raise ValueError(f"Circuit {i} {c} not valid for backend {self._name}")
            
        res = []
        if type(shots) is int:
            shots_ls: list[int] = [shots for _ in range(len(circuits))]
        elif type(shots) is list:
            shots_ls = shots
        else:
            raise ValueError("Invalid shots argument.")

        if not asynchronous:
            state = [result.get_state() for result in self._backend.run_circuits(cs, n_shots=shots)]
                
            for i,circ in enumerate(circuits):
                r = Result(backend=self, circuit=circ, shots=shots_ls[i], data=state[i], completed=True, statevector=True)
                res.append(r)
        else:
            handlers = self._backend.process_circuits(cs, n_shots=shots)
            for i,circ in enumerate(circuits):
                r = Result(backend=self, circuit=circ, shots=shots_ls[i], data=handlers[i], completed=False, statevector=True)
                res.append(r)
                
        if len(res) == 1:
            return res[0]
        else:
            return res
    
    def is_valid(self, circuit: Circuit) -> bool:
        """Check if the circuit is valid for the backend."""
        
        if not isinstance(circuit, Circuit):
            circuit = Circuit(circuit)
        
        c = (Translator().translate(circuit, "pytket")).get()
        return bool(self._backend.valid_circuit(c))
    
    def is_ready(self, result: Result) -> bool:
        return self._backend.circuit_status(result._data).status == StatusEnum.COMPLETED
    
    def get_result(self, result: Result) -> Result:
        """Return the result of a circuit."""
        
        if result.backend() != self:
            raise ValueError("Result not from this backend.")
        
        if not self.is_ready(result):
            raise ValueError("Result is not ready.")
        state = self._backend.get_result(result._data).get_state()
        return Result(backend=self, circuit=result.circuit(), shots=result.shots(), data=state, completed=True, statevector=True)  
    
    def info(self) -> BackendInfo:
        """Return information about the backend."""
        return self._info
    
    def to_tk(self) -> TK_Backend:
        """Return the backend as a pytket backend."""
        return self._backend
    

class Local(Provider):
    
    def __init__(self, token: str) -> None:
        """Initialize an Aer provider."""
        super().__init__(token)
        self._backends : dict[str, Backend] = {}
    
    def available_backends(self) -> list[Backend]:
        """Return a list of available backends."""
        return list(self._backends.values()) # type: ignore
    
    def add_backend(self, backend: Backend) -> None:
        """Add a backend."""
        name = backend.name()
        if name not in self._backends:
            self._backends[name] = backend
    
    def get_backend(self, name: str, instance_name: str | None = None) -> Backend:
        """Return a backend."""
        if name not in self._backends:
            return self.load_backend(name, AerStateBackend)
        else:
            return self._backends[name]