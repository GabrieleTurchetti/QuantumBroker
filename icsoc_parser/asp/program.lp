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
gates2q_speed(ibm_kyoto, 100).

machine(simulator_stabilizer).
status(simulator_stabilizer, online).
technology(simulator_stabilizer, simulator).
language(simulator_stabilizer, openqasm2).
qubits(simulator_stabilizer, 5000).
max_depth(simulator_stabilizer, 100).
max_shots(simulator_stabilizer, 20000).
kWh(simulator_stabilizer, 11).
expected_waiting_time(simulator_stabilizer, 0).
expected_execution_time(simulator_stabilizer, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*1100*S/1000.
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
kWh(simulator_mps, 12).
expected_waiting_time(simulator_mps, 0).
expected_execution_time(simulator_mps, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*1200*S/1000.
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
kWh(simulator_extended_stabilizer, 13).
expected_waiting_time(simulator_extended_stabilizer, 0).
expected_execution_time(simulator_extended_stabilizer, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*1300*S/1000.
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
qubits(ibmq_qasm_simulator, 32).
max_depth(ibmq_qasm_simulator, 100).
max_shots(ibmq_qasm_simulator, 20000).
kWh(ibmq_qasm_simulator, 14).
expected_waiting_time(ibmq_qasm_simulator, 0).
expected_execution_time(ibmq_qasm_simulator, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*1400*S/1000.
expected_cost(ibmq_qasm_simulator, C, Res) :- dispatch(ibmq_qasm_simulator, C, Dispatch), Res = 0*Dispatch/100.
region(ibmq_qasm_simulator, europe).
region(ibmq_qasm_simulator, north_america).
region(ibmq_qasm_simulator, south_america).
region(ibmq_qasm_simulator, asia).
region(ibmq_qasm_simulator, africa).
region(ibmq_qasm_simulator, australia).
gates1q_speed(ibmq_qasm_simulator, 50).
gates2q_speed(ibmq_qasm_simulator, 50).

machine(simulator_statevector).
status(simulator_statevector, online).
technology(simulator_statevector, simulator).
language(simulator_statevector, openqasm2).
qubits(simulator_statevector, 32).
max_depth(simulator_statevector, 100).
max_shots(simulator_statevector, 20000).
kWh(simulator_statevector, 15).
expected_waiting_time(simulator_statevector, 0).
expected_execution_time(simulator_statevector, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*1500*S/1000.
expected_cost(simulator_statevector, C, Res) :- dispatch(simulator_statevector, C, Dispatch), Res = 0*Dispatch/100.
region(simulator_statevector, europe).
region(simulator_statevector, north_america).
region(simulator_statevector, south_america).
region(simulator_statevector, asia).
region(simulator_statevector, africa).
region(simulator_statevector, australia).
gates1q_speed(simulator_statevector, 60).
gates2q_speed(simulator_statevector, 60).

circuit(c1).
circuit_depth(c1, 1).
circuit_lang(c1, openqasm2).
circuit_qubits(c1, 2).
gates1q(c1, 1).
gates2q(c1, 1).
circuit_computer(c1, simulator_mps).

circuit(c2).
circuit_depth(c2, 1).
circuit_lang(c2, openqasm2).
circuit_qubits(c2, 2).
gates1q(c2, 3).
gates2q(c2, 1).
circuit_computer(c2, simulator_statevector).

circuit(c3).
circuit_depth(c3, 1).
circuit_lang(c3, openqasm2).
circuit_qubits(c3, 2).
gates1q(c3, 1).
gates2q(c3, 1).
circuit_computer(c3, simulator_stabilizer).

circuit(c4).
circuit_depth(c4, 1).
circuit_lang(c4, openqasm2).
circuit_qubits(c4, 109).
gates1q(c4, 9).
gates2q(c4, 1).
circuit_computer(c4, ibm_osaka).

circuit(c5).
circuit_depth(c5, 1).
circuit_lang(c5, openqasm2).
circuit_qubits(c5, 2).
gates1q(c5, 3).
gates2q(c5, 1).
circuit_computer(c5, ibmq_qasm_simulator).

circuit(c6).
circuit_depth(c6, 1).
circuit_lang(c6, openqasm2).
circuit_qubits(c6, 2).
gates1q(c6, 1).
gates2q(c6, 1).
circuit_computer(c6, simulator_extended_stabilizer).

circuit(c7).
circuit_depth(c7, 1).
circuit_lang(c7, openqasm2).
circuit_qubits(c7, 5).
gates1q(c7, 9).
gates2q(c7, 1).
circuit_computer(c7, ibm_brisbane).

circuit(c8).
circuit_depth(c8, 1).
circuit_lang(c8, openqasm2).
circuit_qubits(c8, 48).
gates1q(c8, 9).
gates2q(c8, 1).
circuit_computer(c8, ibm_kyoto).

circuit(c9).
circuit_depth(c9, 1).
circuit_lang(c9, openqasm2).
circuit_qubits(c9, 48).
gates1q(c9, 9).
gates2q(c9, 1).
circuit_computer(c9, ibm_sherbrooke).


#show dispatch/3.
#show total_cost/1.
#show total_time/1.
%#show used_computers/1.

packets(0..P) :- total_shots(Total_shots), granularity(Granularity), P = (Total_shots/Granularity).
shots(S) :- packets(P), granularity(Granularity), S = P*Granularity.

1 { compatible(M,C) ; not_compatible(M,C) } 1 :- machine(M), circuit(C), circuit_computer(C,M).

1 { dispatch(M, C, S) : shots(S), S > 0 } 1 :- compatible(M, C). %distribute the shots

:- compatible(M,C), qubits(M, FeatQBits), circuit_qubits(C, Req_qubits), FeatQBits < Req_qubits.
:- compatible(M,C), max_depth(M, FeatDepth), circuit_depth(C, Req_depth), FeatDepth < Req_depth.
:- compatible(M,C), language(M, FeatLang), circuit_lang(C, Req_Leang), FeatLang != Req_Leang.

:- compatible(M,_), status(M, S), S != online.
:- compatible(M,_), max_shots(M, Max), machine_total_load(M, Machine_total_load), Machine_total_load > Max.

:- total_load(V), total_shots(Total_shots), V != Total_shots. %ensure all the shots will be performed
:- total_cost(V), max_cost(Max_cost), V > Max_cost. % stay in the budget
:- total_time(V), max_time(Max_time), V > Max_time. % stay in the budget

shots_difference(V) :- used_computers(Comp), total_shots(T), Ideal = T/Comp, V = #sum{E,M,C : dispatch(M, C, S), E1 = S-Ideal, E = |E1|}.
used_computers(V) :- V = #sum{1,M : dispatch(M,_,S), shots(S), S > 0}.
total_load(V) :- V = #sum{S,M,C : dispatch(M,C,S), compatible(M,C), shots(S)}.
total_cost(V) :- V = #sum{Cost,M,C : expected_cost(M,C,Cost), compatible(M,C), dispatch(M,C,S), S > 0 }.
total_time(Total_time) :- Total_time = #max{ T : compatible(M,C), dispatch(M,C,S), S > 0, machine_total_time(M, C, S, T) }.
machine_total_time(M, C, S, Total_time) :- expected_waiting_time(M, Expected_waiting_time), expected_execution_time(M, C, S, Expected_execution_time), Total_time = (Expected_waiting_time) + (Expected_execution_time).
machine_total_load(M, Machine_total_load) :- machine(M), Machine_total_load = #sum{S,C : dispatch(M, C, S)}.

total_energy_cost(Total_energy_cost) :- Total_energy_cost = #sum{ E, M : compatible(M,C), dispatch(M,C,S), shots(S), S > 0, energy_cost(M, C, S, E) }.
energy_cost(M, C, S, Energy_cost) :- dispatch(M,C,S), shots(S), technology(M, superconductor), gates1q(C,G1), gates2q(C,G2), gates1q_speed(M,G1_speed), gates2q_speed(M,G2_speed), kWh(M, K), Energy_cost = S*(G1_speed*G1 + G2_speed*G2)*K/1000000000.
energy_cost(M, C, S, Energy_cost) :- dispatch(M,C,S), shots(S), technology(M, trapped_ions), gates1q(C,G1), gates2q(C,G2), gates1q_speed(M,G1_speed), gates2q_speed(M,G2_speed), kWh(M, K), Energy_cost = S*(G1_speed*G1 + G2_speed*G2)*K/1000000000.
energy_cost(M, C, S, Energy_cost) :- dispatch(M,C,S), shots(S), technology(M, neutral_atoms), gates1q(C,G1), gates2q(C,G2), gates1q_speed(M,G1_speed), gates2q_speed(M,G2_speed), kWh(M, K), Energy_cost = S*(G1_speed*G1 + G2_speed*G2)*K/1000000000.
energy_cost(M, C, S, Energy_cost) :- dispatch(M,C,S), shots(S), technology(M, simulator), gates1q(C,G1), gates2q(C,G2), gates1q_speed(M,G1_speed), gates2q_speed(M,G2_speed), kWh(M, K), Energy_cost = S*(G1_speed*G1 + G2_speed*G2)*K/100000.
#show total_energy_cost/1.

total_shots(10000).
granularity(2000).
max_cost(99999999).
max_time(99999999).
