from abc import ABC, abstractmethod

from ...circuits import Circuit
from ...backends import Backend
from ...translator import Translator

from typing import Any, Optional


class Compiler(ABC):
    
    _translator = Translator()
    
    @staticmethod   
    @abstractmethod
    def _compile(circuit: Circuit, backend: Optional[Backend] = None, optimisation_level: int = 0, initial_placement: list[int] = None) -> Circuit:
        """Compile and optionally optimise the circuit (for a backend)."""
        pass
    
    @staticmethod
    @abstractmethod
    def circuit_type() -> Any:
        pass
    
    @classmethod
    def compile(cls, circuit: Circuit, backend: Optional[Backend] = None, optimisation_level: int = 0, initial_placement: list[int] = None) -> Circuit:
        
        if not isinstance(circuit, Circuit):
            circuit = Circuit(circuit)
        
        circuit_type = circuit.circuit_type()
        language = cls._translator.which(circuit)
        
        if not issubclass(circuit_type, cls.circuit_type()):
            circuit = cls._translator.translate(circuit, cls.circuit_type())
            
        compiled_circuit = cls._compile(circuit, backend, optimisation_level, initial_placement)
        
        if not issubclass(compiled_circuit.circuit_type(), circuit_type):
            compiled_circuit = cls._translator.translate(compiled_circuit, language)
            
        return Circuit(compiled_circuit, circuit, cls)
        
    
    def __str__(self) -> str:
        """Return a string representation of the compiler."""
        return f"Compiler({self.__class__.__name__})"
    
    def __repr__(self) -> str:
        """Return a string representation of the compiler."""
        return self.__str__()