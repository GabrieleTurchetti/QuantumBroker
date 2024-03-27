machine(ibmq_qasm_simulator).
status(ibmq_qasm_simulator, online).
technology(ibmq_qasm_simulator, simulator).
language(ibmq_qasm_simulator, openqasm2).
qubits(ibmq_qasm_simulator, 79).
max_depth(ibmq_qasm_simulator, 100).
kWh(ibmq_qasm_simulator, 5).
expected_waiting_time(ibmq_qasm_simulator, 0).
expected_execution_time(ibmq_qasm_simulator, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*3*S.
expected_cost(ibmq_qasm_simulator, C, Res) :- dispatch(ibmq_qasm_simulator, C, Dispatch), Res = 2*Dispatch.
region(ibmq_qasm_simulator, europe).
gates1q_speed(ibmq_qasm_simulator, 5).
gates2q_speed(ibmq_qasm_simulator, 5).

machine(simulator_extended_stabilizer).
status(simulator_extended_stabilizer, online).
technology(simulator_extended_stabilizer, simulator).
language(simulator_extended_stabilizer, openqasm2).
qubits(simulator_extended_stabilizer, 79).
max_depth(simulator_extended_stabilizer, 100).
kWh(simulator_extended_stabilizer, 5).
expected_waiting_time(simulator_extended_stabilizer, 0).
expected_execution_time(simulator_extended_stabilizer, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*3*S.
expected_cost(simulator_extended_stabilizer, C, Res) :- dispatch(simulator_extended_stabilizer, C, Dispatch), Res = 2*Dispatch.
region(simulator_extended_stabilizer, europe).
gates1q_speed(simulator_extended_stabilizer, 5).
gates2q_speed(simulator_extended_stabilizer, 5).

machine(simulator_mps).
status(simulator_mps, online).
technology(simulator_mps, simulator).
language(simulator_mps, openqasm2).
qubits(simulator_mps, 79).
max_depth(simulator_mps, 100).
kWh(simulator_mps, 5).
expected_waiting_time(simulator_mps, 0).
expected_execution_time(simulator_mps, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*3*S.
expected_cost(simulator_mps, C, Res) :- dispatch(simulator_mps, C, Dispatch), Res = 2*Dispatch.
region(simulator_mps, europe).
gates1q_speed(simulator_mps, 5).
gates2q_speed(simulator_mps, 5).

machine(simulator_stabilizer).
status(simulator_stabilizer, online).
technology(simulator_stabilizer, simulator).
language(simulator_stabilizer, openqasm2).
qubits(simulator_stabilizer, 79).
max_depth(simulator_stabilizer, 100).
kWh(simulator_stabilizer, 5).
expected_waiting_time(simulator_stabilizer, 0).
expected_execution_time(simulator_stabilizer, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*3*S.
expected_cost(simulator_stabilizer, C, Res) :- dispatch(simulator_stabilizer, C, Dispatch), Res = 2*Dispatch.
region(simulator_stabilizer, europe).
gates1q_speed(simulator_stabilizer, 5).
gates2q_speed(simulator_stabilizer, 5).