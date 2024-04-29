machine(ibm_sherbrooke).
status(ibm_sherbrooke, online).
technology(ibm_sherbrooke, superconductor).
qubits(ibm_sherbrooke, 127).
language(ibm_sherbrooke, openqasm2).
kWh(ibm_sherbrooke, 10).
max_shots(ibm_sherbrooke, 20000).
max_depth(ibm_sherbrooke, 100).
expected_waiting_time(ibm_sherbrooke, 0).
expected_execution_time(ibm_sherbrooke, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*1000*S/1000.
expected_cost(ibm_sherbrooke, C, Res) :- dispatch(ibm_sherbrooke, C, Dispatch), Res = 100*Dispatch/1000.
region(ibm_sherbrooke, north_america).
gates1q_speed(ibm_sherbrooke, 10).
gates2q_speed(ibm_sherbrooke, 10).

machine(ibm_brisbane).
status(ibm_brisbane, online).
technology(ibm_brisbane, superconductor).
qubits(ibm_brisbane, 127).
language(ibm_brisbane, openqasm2).
kWh(ibm_brisbane, 10).
max_shots(ibm_brisbane, 20000).
max_depth(ibm_brisbane, 100).
expected_waiting_time(ibm_brisbane, 0).
expected_execution_time(ibm_brisbane, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*1000*S/1000.
expected_cost(ibm_brisbane, C, Res) :- dispatch(ibm_brisbane, C, Dispatch), Res = 100*Dispatch/1000.
region(ibm_brisbane, australia).
gates1q_speed(ibm_brisbane, 10).
gates2q_speed(ibm_brisbane, 10).

machine(ibm_osaka).
status(ibm_osaka, online).
technology(ibm_osaka, superconductor).
language(ibm_osaka, openqasm2).
qubits(ibm_osaka, 127).
kWh(ibm_osaka, 10).
max_shots(ibm_osaka, 20000).
max_depth(ibm_osaka, 100).
expected_waiting_time(ibm_osaka, 0).
expected_execution_time(ibm_osaka, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*1000*S/1000.
expected_cost(ibm_osaka, C, Res) :- dispatch(ibm_osaka, C, Dispatch), Res = 100*Dispatch/1000.
region(ibm_osaka, asia).
gates1q_speed(ibm_osaka, 10).
gates2q_speed(ibm_osaka, 10).

machine(simulator_mps).
status(simulator_mps, online).
technology(simulator_mps, simulator).
language(simulator_mps, openqasm2).
qubits(simulator_mps, 100).
max_depth(simulator_mps, 100).
max_shots(simulator_mps, 20000).
kWh(simulator_mps, 20).
expected_waiting_time(simulator_mps, 0).
expected_execution_time(simulator_mps, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*900*S/1000.
expected_cost(simulator_mps, C, Res) :- dispatch(simulator_mps, C, Dispatch), Res = 0*Dispatch/100.
region(simulator_mps, europe).
region(simulator_mps, north_america).
region(simulator_mps, south_america).
region(simulator_mps, asia).
region(simulator_mps, africa).
region(simulator_mps, australia).
gates1q_speed(simulator_mps, 100).
gates2q_speed(simulator_mps, 100).

machine(simulator_extended_stabilizer).
status(simulator_extended_stabilizer, online).
technology(simulator_extended_stabilizer, simulator).
language(simulator_extended_stabilizer, openqasm2).
qubits(simulator_extended_stabilizer, 63).
max_depth(simulator_extended_stabilizer, 100).
max_shots(simulator_extended_stabilizer, 20000).
kWh(simulator_extended_stabilizer, 30).
expected_waiting_time(simulator_extended_stabilizer, 0).
expected_execution_time(simulator_extended_stabilizer, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*800*S/1000.
expected_cost(simulator_extended_stabilizer, C, Res) :- dispatch(simulator_extended_stabilizer, C, Dispatch), Res = 0*Dispatch/100.
region(simulator_extended_stabilizer, europe).
region(simulator_extended_stabilizer, north_america).
region(simulator_extended_stabilizer, south_america).
region(simulator_extended_stabilizer, asia).
region(simulator_extended_stabilizer, africa).
region(simulator_extended_stabilizer, australia).
gates1q_speed(simulator_extended_stabilizer, 200).
gates2q_speed(simulator_extended_stabilizer, 200).

machine(simulator_statevector).
status(simulator_statevector, online).
technology(simulator_statevector, simulator).
language(simulator_statevector, openqasm2).
qubits(simulator_statevector, 32).
max_depth(simulator_statevector, 100).
max_shots(simulator_statevector, 20000).
kWh(simulator_statevector, 40).
expected_waiting_time(simulator_statevector, 0).
expected_execution_time(simulator_statevector, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*700*S/1000.
expected_cost(simulator_statevector, C, Res) :- dispatch(simulator_statevector, C, Dispatch), Res = 0*Dispatch/100.
region(simulator_statevector, europe).
region(simulator_statevector, north_america).
region(simulator_statevector, south_america).
region(simulator_statevector, asia).
region(simulator_statevector, africa).
region(simulator_statevector, australia).
gates1q_speed(simulator_statevector, 300).
gates2q_speed(simulator_statevector, 300).