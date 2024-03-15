from .circuits.compilers.compilers import *
from ..components.translator import Translator

from qiskit import QuantumCircuit

from typing import Any

tr = Translator()


class CompilationManager:
    
    def __init__(self) -> None:
        """Initialize a translator."""
        self._compilers : dict[str, Compiler] = {}
        
        for g in globals():
            try:
                g = globals()[g]
                if issubclass(g, Compiler) and g is not Compiler: # type: ignore
                    self.register_compiler(g)
            except TypeError:
                pass
                
    def register_compiler(self, compiler: Any) -> None:
        """Register a compiler."""
        self._compilers[compiler.__name__.lower()] = compiler
        
    def compile(self, circuit: Circuit, compiler: Compiler | str, backend: Optional[Backend] = None, optimisation_level: int = 0, initial_placement: list[int] = None) -> Circuit:
        
        if not isinstance(circuit, Circuit):
            circuit = Circuit(circuit)
        
        if isinstance(compiler, str):
            compiler = compiler.lower()
            if compiler not in self._compilers:
                compiler += "compiler"
                if compiler not in self._compilers:
                    raise ValueError(f"Unknown compiler: {compiler}")
            compiler = self._compilers[compiler]
            
        if initial_placement is not None:
            if not isinstance(circuit.get(), QuantumCircuit):
                qc_circuit = tr.translate(circuit.get(), "qiskit")
            else:
                qc_circuit = circuit
            qasm_circuit = tr.translate(qc_circuit.get().decompose().decompose(), "openqasm2")
            max_qubits = max(initial_placement)
            circuit_qubits = len(qc_circuit.get().qubits)
            c = qasm_circuit.get()
            c = c.replace(f"qreg q[{circuit_qubits}];", f"qreg q[{max_qubits+1}];")
            for i in range(circuit_qubits):
                c = c.replace(f"q[{i}]", f"q[{initial_placement[i]}]")
            c = tr.translate(c, circuit)
            circuit = Circuit(c, qc_circuit)
        
        compiled = compiler.compile(circuit, backend, optimisation_level, None)
        
        if not isinstance(compiled, Circuit):
            compiled = Circuit(compiled, circuit, compiler)
            
        return compiled
    
    