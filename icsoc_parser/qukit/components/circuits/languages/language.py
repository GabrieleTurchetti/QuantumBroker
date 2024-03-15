from abc import ABC, abstractmethod

from pytket.circuit import Circuit as pytket_Circuit

from ...circuits import Circuit

from typing import Any

from threading import Lock

class Language(ABC):
    
    _lock = Lock()
    
    @staticmethod   
    @abstractmethod
    def _translate_from(circuit: Circuit) -> Circuit:
        """Translate the circuit from another language."""
        pass
    
    @staticmethod   
    @abstractmethod
    def _translate_to(circuit: Circuit) -> Circuit:
        """Translate the circuit to another language."""
        pass
    
    @staticmethod
    @abstractmethod
    def circuit_type() -> Any:
        pass
    
    @classmethod   
    def translate(cls, circuit: Circuit) -> Circuit:
        """Translate the circuit from/to another language."""
        
        if not isinstance(circuit, Circuit):
            circuit = Circuit(circuit)
        
        if isinstance(circuit.get(), cls.circuit_type()):
            with cls._lock:
                translated = cls._translate_from(circuit)
            assert isinstance(translated.get(), pytket_Circuit)
            return Circuit(translated)
        elif isinstance(circuit.get(), pytket_Circuit):
            with cls._lock:
                translated = cls._translate_to(circuit)
            assert isinstance(translated.get(), cls.circuit_type())
            return Circuit(translated)
        else:
            raise TypeError(f"Can't translate {circuit} ({circuit.circuit_type().__name__}) to {cls.circuit_type().__name__}.")
        
    
    def __str__(self) -> str:
        """Return a string representation of the language."""
        return f"Language({self.__class__.__name__})"
    
    def __repr__(self) -> str:
        """Return a string representation of the language."""
        return self.__str__()