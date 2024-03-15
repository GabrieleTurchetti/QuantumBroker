import math
import random

import pytket.backends

from abc import ABC, abstractmethod

from ..circuits import Circuit

from typing import Any, Optional



class Result:
    def __init__(self, backend: 'Backend', circuit: Circuit, shots: int, data: Any, completed: bool = False, statevector: bool = False) -> None:
        self._backend = backend
        self._circuit = Circuit(circuit)
        self._shots = shots
        self._data = data
        self._completed = completed
        self._statevector = statevector
        
    def backend(self) -> 'Backend':
        return self._backend
    
    def circuit(self) -> Circuit:
        return self._circuit
    
    def shots(self) -> int:
        return self._shots
    
    def counts(self) -> dict[str, int]: # type: ignore
        counts: dict[str, int] = {}
        if self.completed():
            if self.is_statevector():
                probs = self.distribution()
                counts = {}
                for _ in range(self._shots):
                    r = random.random()
                    s = 0.
                    for k,v in probs.items():
                        s += v 
                        if r < s:
                            if k in counts:
                                counts[k] += 1
                            else:
                                counts[k] = 1
                            break
                return counts
            else:
                for k,v in self._data.items():
                    if type(v) is not int:
                        raise RuntimeError("Result not completed.")
                    counts[str(k)] = int(v)
                return counts
        else:
            raise RuntimeError("Result not completed.")
        
    def statevector(self) -> list[complex]:
        if self.completed():
            if self.is_statevector():
                return self._data
            else:
                raise RuntimeError("Statevector not available.")
        else:
            raise RuntimeError("Result not completed.")
        
    def distribution(self) -> dict[str, float]:
        if self.completed():
            if not self.is_statevector():
                return {k: v/self._shots for k,v in self.counts().items()}
            else:
                probs : dict[str, float] = {}
                qubits = int(math.log2(len(self._data)))
                for i in range(2**(qubits)):
                    probs[bin(i)[2:].zfill(qubits)] = abs(self._data[i])**2
                return probs
        else:
            raise RuntimeError("Result not completed.")
    
    def completed(self) -> bool:
        return self._completed
    
    def is_statevector(self) -> bool:
        return self._statevector

    def update(self) -> bool:
        """Return the result of a circuit."""
        if not self.completed():
            if self._backend.is_ready(self):
                self._data = self._backend.get_result(self)._data
                self._completed = True
            else:
                return False
        
        return True
    
    def __str__(self) -> str:
        if self.completed():
            return f"Result(backend={self._backend}, circuit={self._circuit}, shots={self._shots}, data={self._data}), completed={self._completed}), statevector={self._statevector})"
        else:
            return f"Result(backend={self._backend}, circuit={self._circuit}, shots={self._shots}, data=..., completed={self._completed}), statevector={self._statevector})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def to_dict(self) -> dict:
        return {
            "provider": self._backend.provider().name(),
            "backend": self._backend.name(),
            "circuit": self._circuit.get(),
            "shots": self._shots,
            "data": self._data,
            "completed": self._completed,
            "statevector": self._statevector
        }

class Provider(ABC):
    """Abstract base class for providers."""
    
    def __init__(self, token: str) -> None:
        """Initialize a provider."""
        self._token = token
    
    @abstractmethod
    def available_backends(self) -> list['Backend']:
        """Return a list of available backends."""
        pass
    
    @abstractmethod
    def get_backend(self, name: str) -> 'Backend':
        """Return a backend."""
        pass
    
    def __str__(self) -> str:
        """Return a string representation of the provider."""
        if len(str(self._token)) < 5:
            return f"{self.__class__.__name__}(token={self._token})"
        return f"{self.__class__.__name__}(token={self._token[:5]}...)"
    
    def __repr__(self) -> str:
        """Return a string representation of the provider."""
        return self.__str__()
    
    def name(self) -> str:
        """Return the name of the provider."""
        return self.__class__.__name__
    
class BackendInfo:
    
    def gateset(self) -> Optional[dict[str, int]]:
        return None
    
    def qubits(self) -> Optional[int]:
        return None
    
    def max_shots(self) -> Optional[int]:
        return None
    
    def coupling_map(self) -> Optional[list[tuple[int, int]]]:
        return None
    
    def properties(self) -> Optional[dict[str, Any]]:
        return None
    
    def __str__(self) -> str:
        return f"BackendInfo(gateset={self.gateset()}, qubits={self.qubits()}, max_shots={self.max_shots()}, coupling_map={self.coupling_map()}, properties={self.properties()})"
    
    def __repr__(self) -> str:
        return self.__str__()

class Backend(ABC):
    """Abstract base class for backends."""
    
    def __init__(self, name: str, provider: Provider, instance_name: str | None = None) -> None:
        """Initialize a backend."""
        self._name = name
        self._provider = provider
        self._instance_name = instance_name
    
    @abstractmethod
    def run(self, circuits: Circuit | list[Circuit], shots: int | list[int] = 1, asynchronous: bool = False) -> Result | list[Result]:
        """Run the circuits on the backend."""
        pass
    
    @abstractmethod
    def is_valid(self, circuit: Circuit) -> bool:
        """Check if the circuit is valid for the backend."""
        pass
    
    @abstractmethod
    def get_result(self, result: Result) -> Result:
        """Return the result of a circuit."""
        pass
    
    @abstractmethod
    def is_ready(self, result: Result) -> bool:
        """Check if the result is ready."""
        pass
    
    @abstractmethod
    def info(self) -> BackendInfo:
        """Return information about the backend."""
        pass
    
    @abstractmethod
    def to_tk(self) -> pytket.backends.Backend:
        """Return the backend as a tket backend."""
        pass
    
    def provider(self) -> Provider:
        """Return the provider of the backend."""
        return self._provider
    
    def name(self) -> str:
        """Return the name of the backend."""
        if self._instance_name is not None:
            return self._instance_name
        return self._name
    
    def device(self) -> str:
        """Return the device of the backend."""
        return self._name
    
    def __str__(self) -> str:
        """Return a string representation of the backend."""
        return f"{self.__class__.__name__}(name={self._name}, provider={self._provider})"
    
    def __repr__(self) -> str:
        """Return a string representation of the backend."""
        return self.__str__()
    