import qiskit

import pytket.circuit
import pytket.backends
import pytket.architecture
import pytket.placement

from .compiler import Compiler
from ...circuits import Circuit
from ...backends import Backend

from typing import Any, Optional


class QiskitCompiler(Compiler):
    """A compiler for Qiskit."""
    
    @staticmethod
    def circuit_type() -> Any:
        return qiskit.QuantumCircuit
    
    @staticmethod
    def _compile(circuit: Circuit, backend: Optional[Backend] = None, optimisation_level: int = 0, initial_placement: list[int] = None) -> Circuit:
        circuit = circuit.get()
        
        backend_info = None
        if backend is not None:
            backend_info = backend.info()
            
        basis_gates = None
        coupling_map = None
        backend_properties = None
        if backend_info is not None:
            basis_gates = [x.lower() for x in backend_info.gateset()] if backend_info.gateset() is not None else None # type: ignore
            coupling_map = backend_info.coupling_map()
            backend_properties = backend_info.properties()
            
        circuit = qiskit.transpile(circuit, backend_properties=backend_properties, basis_gates=basis_gates, coupling_map=coupling_map, optimization_level=optimisation_level, initial_layout=initial_placement)
        
        return Circuit(circuit)
    
class TketCompiler(Compiler):
    
    @staticmethod
    def circuit_type() -> Any:
        return pytket.circuit.Circuit
    
    @staticmethod
    def _compile(circuit: Circuit, backend: Optional[Backend] = None, optimisation_level: int = 0, initial_placement: list[int] = None) -> Circuit:
        tk_circuit = circuit.get() 
        
        if backend is None:
            return Circuit(circuit)
        
        _backend = backend.to_tk() # type: ignore
        
        if _backend is None:
            return Circuit(circuit)
        
        _circuit = _backend.get_compiled_circuit(tk_circuit, optimisation_level=optimisation_level)
        
        map = {}
        if initial_placement is not None:
            for i, q in enumerate(initial_placement):
                map[i] = q
        
        pytket.placement.Placement.from_dict(map).place(_circuit)
        
        return Circuit(_circuit)
        