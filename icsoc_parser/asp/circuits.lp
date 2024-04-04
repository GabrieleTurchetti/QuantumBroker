circuit(c1).
circuit_depth(c1, 1).
circuit_lang(c1, openqasm2).
circuit_qubits(c1, 2).
gates1q(c1, 1).
gates2q(c1, 1).
circuit_computer(c1, simulator_extended_stabilizer).

circuit(c2).
circuit_depth(c2, 1).
circuit_lang(c2, openqasm2).
circuit_qubits(c2, 2).
gates1q(c2, 1).
gates2q(c2, 1).
circuit_computer(c2, simulator_mps).

circuit(c3).
circuit_depth(c3, 1).
circuit_lang(c3, openqasm2).
circuit_qubits(c3, 2).
gates1q(c3, 3).
gates2q(c3, 1).
circuit_computer(c3, simulator_statevector).

circuit(c4).
circuit_depth(c4, 1).
circuit_lang(c4, openqasm2).
circuit_qubits(c4, 2).
gates1q(c4, 1).
gates2q(c4, 1).
circuit_computer(c4, simulator_stabilizer).

circuit(c5).
circuit_depth(c5, 1).
circuit_lang(c5, openqasm2).
circuit_qubits(c5, 2).
gates1q(c5, 9).
gates2q(c5, 1).
circuit_computer(c5, ibm_brisbane).

circuit(c6).
circuit_depth(c6, 1).
circuit_lang(c6, openqasm2).
circuit_qubits(c6, 2).
gates1q(c6, 9).
gates2q(c6, 1).
circuit_computer(c6, ibm_kyoto).

circuit(c7).
circuit_depth(c7, 1).
circuit_lang(c7, openqasm2).
circuit_qubits(c7, 2).
gates1q(c7, 9).
gates2q(c7, 1).
circuit_computer(c7, ibm_osaka).

circuit(c8).
circuit_depth(c8, 1).
circuit_lang(c8, openqasm2).
circuit_qubits(c8, 2).
gates1q(c8, 3).
gates2q(c8, 1).
circuit_computer(c8, ibmq_qasm_simulator).

