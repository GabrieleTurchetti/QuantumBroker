machine(ibm_brisbane).
status(ibm_brisbane, online).
technology(ibm_brisbane, superconductor).
qubits(ibm_brisbane, 127).
language(ibm_brisbane, openqasm2).
kWh(ibm_brisbane, 3).
max_shots(ibm_brisbane, 20000).
max_depth(ibm_brisbane, 100).
expected_waiting_time(ibm_brisbane, 0).
expected_execution_time(ibm_brisbane, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*5*S.
expected_fidelity(ibm_brisbane, 0).
expected_cost(ibm_brisbane, C, Res) :- dispatch(ibm_brisbane, C, Dispatch), Res = 1*Dispatch.
region(ibm_brisbane, australia).
gates1q_speed(ibm_brisbane, 3).
gates2q_speed(ibm_brisbane, 3).

machine(ibm_osaka).
status(ibm_osaka, online).
technology(ibm_osaka, superconductor).
language(ibm_osaka, openqasm2).
qubits(ibm_osaka, 127).
kWh(ibm_osaka, 1).
max_shots(ibm_osaka, 20000).
max_depth(ibm_osaka, 100).
expected_waiting_time(ibm_osaka, 0).
expected_execution_time(ibm_osaka, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*5*S.
expected_cost(ibm_osaka, C, Res) :- dispatch(ibm_osaka, C, Dispatch), Res = 5*Dispatch.
region(ibm_osaka, asia).
gates1q_speed(ibm_osaka, 2).
gates2q_speed(ibm_osaka, 2).

machine(ibm_kyoto).
status(ibm_kyoto, online).
technology(ibm_kyoto, superconductor).
language(ibm_kyoto, openqasm3).
language(ibm_kyoto, openqasm2).
qubits(ibm_kyoto, 7).
kWh(ibm_kyoto, 2).
max_shots(ibm_kyoto, 20000).
max_depth(ibmibm_kyoto_perth, 100).
expected_waiting_time(ibm_kyoto, 0).
expected_execution_time(ibm_kyoto, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*10*S.
expected_cost(ibm_kyoto, C, Res) :- dispatch(ibm_kyoto, C, Dispatch), Res = 0*Dispatch.
region(ibm_kyoto, asia).
gates1q_speed(ibm_kyoto, 3).
gates2q_speed(ibm_kyoto, 3).

machine(simulator_stabilizer).
status(simulator_stabilizer, online).
technology(simulator_stabilizer, simulator).
language(simulator_stabilizer, openqasm2).
qubits(simulator_stabilizer, 5000).
max_depth(simulator_stabilizer, 100).
max_shots(simulator_stabilizer, 20000).
kWh(simulator_stabilizer, 5).
expected_waiting_time(simulator_stabilizer, 0).
expected_execution_time(simulator_stabilizer, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*3*S.
expected_cost(simulator_stabilizer, C, Res) :- dispatch(simulator_stabilizer, C, Dispatch), Res = 2*Dispatch.
region(simulator_stabilizer, europe).
region(simulator_stabilizer, north_america).
region(simulator_stabilizer, south_america).
region(simulator_stabilizer, asia).
region(simulator_stabilizer, africa).
region(simulator_stabilizer, australia).
gates1q_speed(simulator_stabilizer, 5).
gates2q_speed(simulator_stabilizer, 5).

machine(simulator_mps).
status(simulator_mps, online).
technology(simulator_mps, simulator).
language(simulator_mps, openqasm2).
qubits(simulator_mps, 100).
max_depth(simulator_mps, 100).
max_shots(simulator_mps, 20000).
kWh(simulator_mps, 5).
expected_waiting_time(simulator_mps, 0).
expected_execution_time(simulator_mps, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*3*S.
expected_cost(simulator_mps, C, Res) :- dispatch(simulator_mps, C, Dispatch), Res = 2*Dispatch.
region(simulator_mps, europe).
region(simulator_mps, north_america).
region(simulator_mps, south_america).
region(simulator_mps, asia).
region(simulator_mps, africa).
region(simulator_mps, australia).
gates1q_speed(simulator_mps, 5).
gates2q_speed(simulator_mps, 5).

machine(simulator_statevector).
status(simulator_statevector, online).
technology(simulator_statevector, simulator).
language(simulator_statevector, openqasm2).
qubits(simulator_statevector, 32).
max_depth(simulator_statevector, 100).
max_shots(simulator_statevector, 20000).
kWh(simulator_statevector, 5).
expected_waiting_time(simulator_statevector, 0).
expected_execution_time(simulator_statevector, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*3*S.
expected_cost(simulator_statevector, C, Res) :- dispatch(simulator_statevector, C, Dispatch), Res = 2*Dispatch.
region(simulator_statevector, europe).
region(simulator_statevector, north_america).
region(simulator_statevector, south_america).
region(simulator_statevector, asia).
region(simulator_statevector, africa).
region(simulator_statevector, australia).
gates1q_speed(simulator_statevector, 5).
gates2q_speed(simulator_statevector, 5).