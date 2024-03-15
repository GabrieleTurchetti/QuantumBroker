from typing import Any, Optional


class Circuit:
    """Abstract base class for circuits."""
    
    def __init__(self, circuit: Any, source: Optional['Circuit'] = None, compiler: Optional[Any] = None) -> None:
        """Initialize a circuit."""
        
        self._compiled = source is not None and compiler is not None
        
        self._source = source
        self._compiler = compiler
        
        if isinstance(circuit, Circuit):
            self._source = circuit.source()
            self._compiler = circuit.compiler()
            self._compiled = circuit.compiled()
            circuit = circuit.get()
            
        self._circuit = circuit
        
        #TODO: What to do with optimisation level? Different field or different compilers for different optimisation levels?
        
    def get(self) -> Any:
        """Return the circuit."""
        return self._circuit
    
    def circuit_type(self) -> Any:
        """Return the type of the circuit."""
        return self._circuit.__class__
    
    def compiled(self) -> bool:
        """Return whether the circuit is compiled."""
        return self._compiled
    
    def source(self) -> Optional['Circuit']:
        """Return the source circuit."""
        return self._source
    
    def compiler(self) -> Optional[Any]:
        """Return the compiler used to compile the circuit."""
        return self._compiler

    def __str__(self) -> str:
        """Return a string representation of the circuit."""
        c = str(self._circuit)
        c.replace("\n", " ")
        if len(c) > 20:
            c = c[:20] + "..."
        return f"Circuit({self.circuit_type().__name__}({c}))"
    
    def __repr__(self) -> str:
        """Return a string representation of the circuit."""
        return self.__str__()