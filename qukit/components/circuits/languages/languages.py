import tempfile

from pytket.circuit import Circuit as pytket_Circuit 
from pytket.qasm import circuit_from_qasm_str, circuit_to_qasm_str # type: ignore
from pytket.quipper import circuit_from_quipper # type: ignore

from pytket.extensions.braket import braket_to_tk, tk_to_braket # type: ignore
from braket.circuits import Circuit as braket_Circuit

from ...backends.IonQBackend.pytket.extensions.ionq.backends.ionq import tk_to_ionq 

from pytket.extensions.qiskit import qiskit_to_tk, tk_to_qiskit # type: ignore
from qiskit import QuantumCircuit as qiskit_Circuit

from pytket.extensions.cirq import cirq_to_tk, tk_to_cirq # type: ignore
from cirq import Circuit as cirq_Circuit # type: ignore

from pytket.extensions.pyquil import pyquil_to_tk, tk_to_pyquil # type: ignore
from pyquil import Program as pyquil_Program # type: ignore

from pytket.extensions.pennylane import pennylane_to_tk # type: ignore
from pennylane.operation import Operation as pennylane_operation

from pytket.qir import pytket_to_qir # type: ignore

from qukit.components.circuits import Circuit

from .language import Language
from ...circuits import Circuit

from typing import Any


class PytketLanguage(Language):
    """The pytket language."""

    @staticmethod
    def _translate_from(circuit: Circuit) -> Circuit:
        return circuit
        
    @staticmethod
    def _translate_to(circuit: Circuit) -> Circuit:
        return circuit
        
    @staticmethod
    def circuit_type() -> Any:
        return pytket_Circuit
    
    @staticmethod
    def can_translate(circuit: Circuit) -> bool:
        return isinstance(circuit.get(), pytket_Circuit)
    
class BraketLanguage(Language):
    
    @staticmethod
    def _translate_from(circuit: Circuit) -> Circuit:
        return Circuit(braket_to_tk(circuit.get()))
    
    @staticmethod
    def _translate_to(circuit: Circuit) -> Circuit:
        return Circuit(tk_to_braket(circuit.get()))
        
    @staticmethod
    def circuit_type() -> Any:
        return braket_Circuit
    
    @staticmethod
    def can_translate(circuit: Circuit) -> bool:
        return isinstance(circuit.get(), braket_Circuit)
    
class IonQLanguage(Language):
    
    @staticmethod
    def _translate_from(circuit: Circuit) -> Circuit:
        raise NotImplementedError("IonQ -> pytket not implemented")
    
    @staticmethod
    def _translate_to(circuit: Circuit) -> Circuit:
        return Circuit(tk_to_ionq(circuit.get()))
        
    @staticmethod
    def circuit_type() -> Any:
        return tuple
    
    def can_translate(circuit: Circuit) -> bool:
        return False # Currently not supported
    
class QiskitLanguage(Language):
    
    @staticmethod
    def _translate_from(circuit: Circuit) -> Circuit:
        return Circuit(qiskit_to_tk(circuit.get()))
    
    @staticmethod
    def _translate_to(circuit: Circuit) -> Circuit:
        return Circuit(tk_to_qiskit(circuit.get()))
        
    @staticmethod
    def circuit_type() -> Any:
        return qiskit_Circuit
    
    @staticmethod
    def can_translate(circuit: Circuit) -> bool:
        return isinstance(circuit.get(), qiskit_Circuit)
    
class CirqLanguage(Language):
    
    @staticmethod
    def _translate_from(circuit: Circuit) -> Circuit:
        return Circuit(cirq_to_tk(circuit.get()))
    
    @staticmethod
    def _translate_to(circuit: Circuit) -> Circuit:
        return Circuit(tk_to_cirq(circuit.get()))
        
    @staticmethod
    def circuit_type() -> Any:
        return cirq_Circuit
    
    def can_translate(circuit: Circuit) -> bool:
        return isinstance(circuit.get(), cirq_Circuit)
    
    
class OpenQasm2Language(Language):
    
    @staticmethod
    def _translate_from(circuit: Circuit) -> Circuit:
        return Circuit(circuit_from_qasm_str(circuit.get()))
    
    @staticmethod
    def _translate_to(circuit: Circuit) -> Circuit:
        return Circuit(circuit_to_qasm_str(circuit.get()))
        
    @staticmethod
    def circuit_type() -> Any:
        return str
    
    def can_translate(circuit: Circuit) -> bool:
        if not isinstance(circuit.get(), str):
            return False
        else:
            try:
                circuit_from_qasm_str(circuit.get())
                return True
            except Exception as e:
                print("!!!",e)
                print(circuit.get())
                input()
                return False
    
class PyQuilLanguage(Language):
    
    @staticmethod
    def _translate_from(circuit: Circuit) -> Circuit:
        return Circuit(pyquil_to_tk(circuit.get()))
    
    @staticmethod
    def _translate_to(circuit: Circuit) -> Circuit:
        return Circuit(tk_to_pyquil(circuit.get()))
        
    @staticmethod
    def circuit_type() -> Any:
        return pyquil_Program
    
    @staticmethod
    def can_translate(circuit: Circuit) -> bool:
        return isinstance(circuit.get(), pyquil_Program)
    
class PennyLaneLanguage(Language):
    
    @staticmethod
    def _translate_from(circuit: Circuit) -> Circuit:
        # return Circuit(pennylane_to_tk(circuit.get()))
        raise NotImplementedError("PennyLane -> pytket not implemented")
    
    @staticmethod
    def _translate_to(circuit: Circuit) -> Circuit:
        raise NotImplementedError("pytket -> PennyLane not implemented")
        
    @staticmethod
    def circuit_type() -> Any:
        return pennylane_operation
    
    @staticmethod
    def can_translate(circuit: Circuit) -> bool:
        return isinstance(circuit.get(), pennylane_operation)
    
class QIRLanguage(Language):
    
    @staticmethod
    def _translate_from(circuit: Circuit) -> Circuit:
        raise NotImplementedError("QIR -> pytket not implemented")
    
    @staticmethod
    def _translate_to(circuit: Circuit) -> Circuit:
        return Circuit(pytket_to_qir(circuit.get()))
        
    @staticmethod
    def circuit_type() -> Any:
        return str | bytes
    
    @staticmethod
    def can_translate(circuit: Circuit) -> bool:
        return False # Currently not supported
    
class QuilLanguage(Language):
    
    @staticmethod
    def _translate_from(circuit: Circuit) -> Circuit:
        return Circuit(pyquil_to_tk(pyquil_Program(circuit.get())))
    
    @staticmethod
    def _translate_to(circuit: Circuit) -> Circuit:
        return Circuit(tk_to_pyquil(circuit.get()).out())
        
    @staticmethod
    def circuit_type() -> Any:
        return str
    
    @staticmethod
    def can_translate(circuit: Circuit) -> bool:
        if not isinstance(circuit.get(), str):
            return False
        else:
            try:
                pyquil_Program(circuit.get())
                return True
            except:
                return False
    
class QuipperLanguage(Language):
        
        @staticmethod
        def _translate_from(circuit: Circuit) -> Circuit:
            with tempfile.NamedTemporaryFile("w", suffix=".qpy") as f:
                f.write(circuit.get())
                f.flush()
                return Circuit(circuit_from_quipper(f.name))
        
        @staticmethod
        def _translate_to(circuit: Circuit) -> Circuit:
            raise NotImplementedError("pytket -> Quipper not implemented")
            
        @staticmethod
        def circuit_type() -> Any:
            return str
        
        @staticmethod
        def can_translate(circuit: Circuit) -> bool:
            if not isinstance(circuit.get(), str):
                return False
            else:
                try:
                    with tempfile.NamedTemporaryFile("w", suffix=".qpy") as f:
                        f.write(circuit.get())
                        f.flush()
                        circuit_from_quipper(f.name)
                    return True
                except:
                    return False