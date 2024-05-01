machine(ibm_kyoto).
status(ibm_kyoto, online).
technology(ibm_kyoto, superconductor).
qubits(ibm_kyoto, 127).
language(ibm_kyoto, openqasm2).
kWh(ibm_kyoto, 10).
max_shots(ibm_kyoto, 20000).
max_depth(ibm_kyoto, 100).
expected_waiting_time(ibm_kyoto, 0).
expected_execution_time(ibm_kyoto, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*1000*S/1000.
expected_cost(ibm_kyoto, C, Res) :- dispatch(ibm_kyoto, C, Dispatch), Res = 100*Dispatch/1000.
region(ibm_kyoto, asia).
gates1q_speed(ibm_kyoto, 10).
gates2q_speed(ibm_kyoto, 10).

machine(simulator_stabilizer).
status(simulator_stabilizer, online).
technology(simulator_stabilizer, simulator).
language(simulator_stabilizer, openqasm2).
qubits(simulator_stabilizer, 5000).
max_depth(simulator_stabilizer, 100).
max_shots(simulator_stabilizer, 20000).
kWh(simulator_stabilizer, 20).
expected_waiting_time(simulator_stabilizer, 0).
expected_execution_time(simulator_stabilizer, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*700*S/1000.
expected_cost(simulator_stabilizer, C, Res) :- dispatch(simulator_stabilizer, C, Dispatch), Res = 0*Dispatch/100.
region(simulator_stabilizer, europe).
region(simulator_stabilizer, north_america).
region(simulator_stabilizer, south_america).
region(simulator_stabilizer, asia).
region(simulator_stabilizer, africa).
region(simulator_stabilizer, australia).
gates1q_speed(simulator_stabilizer, 20).
gates2q_speed(simulator_stabilizer, 20).

machine(simulator_mps).
status(simulator_mps, online).
technology(simulator_mps, simulator).
language(simulator_mps, openqasm2).
qubits(simulator_mps, 100).
max_depth(simulator_mps, 100).
max_shots(simulator_mps, 20000).
kWh(simulator_mps, 30).
expected_waiting_time(simulator_mps, 0).
expected_execution_time(simulator_mps, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*800*S/1000.
expected_cost(simulator_mps, C, Res) :- dispatch(simulator_mps, C, Dispatch), Res = 0*Dispatch/100.
region(simulator_mps, europe).
region(simulator_mps, north_america).
region(simulator_mps, south_america).
region(simulator_mps, asia).
region(simulator_mps, africa).
region(simulator_mps, australia).
gates1q_speed(simulator_mps, 30).
gates2q_speed(simulator_mps, 30).

machine(simulator_extended_stabilizer).
status(simulator_extended_stabilizer, online).
technology(simulator_extended_stabilizer, simulator).
language(simulator_extended_stabilizer, openqasm2).
qubits(simulator_extended_stabilizer, 63).
max_depth(simulator_extended_stabilizer, 100).
max_shots(simulator_extended_stabilizer, 20000).
kWh(simulator_extended_stabilizer, 40).
expected_waiting_time(simulator_extended_stabilizer, 0).
expected_execution_time(simulator_extended_stabilizer, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*900*S/1000.
expected_cost(simulator_extended_stabilizer, C, Res) :- dispatch(simulator_extended_stabilizer, C, Dispatch), Res = 0*Dispatch/100.
region(simulator_extended_stabilizer, europe).
region(simulator_extended_stabilizer, north_america).
region(simulator_extended_stabilizer, south_america).
region(simulator_extended_stabilizer, asia).
region(simulator_extended_stabilizer, africa).
region(simulator_extended_stabilizer, australia).
gates1q_speed(simulator_extended_stabilizer, 40).
gates2q_speed(simulator_extended_stabilizer, 40).

machine(ibmq_qasm_simulator).
status(ibmq_qasm_simulator, online).
technology(ibmq_qasm_simulator, simulator).
language(ibmq_qasm_simulator, openqasm2).
qubits(ibmq_qasm_simulator, 100).
max_depth(ibmq_qasm_simulator, 100).
max_shots(ibmq_qasm_simulator, 20000).
kWh(ibmq_qasm_simulator, 30).
expected_waiting_time(ibmq_qasm_simulator, 0).
expected_execution_time(ibmq_qasm_simulator, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*800*S/1000.
expected_cost(ibmq_qasm_simulator, C, Res) :- dispatch(ibmq_qasm_simulator, C, Dispatch), Res = 0*Dispatch/100.
region(ibmq_qasm_simulator, europe).
region(ibmq_qasm_simulator, north_america).
region(ibmq_qasm_simulator, south_america).
region(ibmq_qasm_simulator, asia).
region(ibmq_qasm_simulator, africa).
region(ibmq_qasm_simulator, australia).
gates1q_speed(ibmq_qasm_simulator, 30).
gates2q_speed(ibmq_qasm_simulator, 30).

machine(simulator_statevector).
status(simulator_statevector, online).
technology(simulator_statevector, simulator).
language(simulator_statevector, openqasm2).
qubits(simulator_statevector, 63).
max_depth(simulator_statevector, 100).
max_shots(simulator_statevector, 20000).
kWh(simulator_statevector, 40).
expected_waiting_time(simulator_statevector, 0).
expected_execution_time(simulator_statevector, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*900*S/1000.
expected_cost(simulator_statevector, C, Res) :- dispatch(simulator_statevector, C, Dispatch), Res = 0*Dispatch/100.
region(simulator_statevector, europe).
region(simulator_statevector, north_america).
region(simulator_statevector, south_america).
region(simulator_statevector, asia).
region(simulator_statevector, africa).
region(simulator_statevector, australia).
gates1q_speed(simulator_statevector, 40).
gates2q_speed(simulator_statevector, 40).