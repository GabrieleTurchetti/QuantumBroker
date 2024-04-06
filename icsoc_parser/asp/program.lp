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
circuit(c1).
circuit_depth(c1, 1).
circuit_lang(c1, openqasm2).
circuit_qubits(c1, 2).
gates1q(c1, 3).
gates2q(c1, 1).
circuit_computer(c1, simulator_statevector).

circuit(c2).
circuit_depth(c2, 1).
circuit_lang(c2, openqasm2).
circuit_qubits(c2, 2).
gates1q(c2, 1).
gates2q(c2, 1).
circuit_computer(c2, simulator_stabilizer).

circuit(c3).
circuit_depth(c3, 1).
circuit_lang(c3, openqasm2).
circuit_qubits(c3, 52).
gates1q(c3, 9).
gates2q(c3, 1).
circuit_computer(c3, ibm_brisbane).

circuit(c4).
circuit_depth(c4, 1).
circuit_lang(c4, openqasm2).
circuit_qubits(c4, 46).
gates1q(c4, 9).
gates2q(c4, 1).
circuit_computer(c4, ibm_kyoto).

circuit(c5).
circuit_depth(c5, 1).
circuit_lang(c5, openqasm2).
circuit_qubits(c5, 30).
gates1q(c5, 9).
gates2q(c5, 1).
circuit_computer(c5, ibm_osaka).

circuit(c6).
circuit_depth(c6, 1).
circuit_lang(c6, openqasm2).
circuit_qubits(c6, 2).
gates1q(c6, 3).
gates2q(c6, 1).
circuit_computer(c6, ibmq_qasm_simulator).

circuit(c7).
circuit_depth(c7, 1).
circuit_lang(c7, openqasm2).
circuit_qubits(c7, 2).
gates1q(c7, 1).
gates2q(c7, 1).
circuit_computer(c7, simulator_extended_stabilizer).

circuit(c8).
circuit_depth(c8, 1).
circuit_lang(c8, openqasm2).
circuit_qubits(c8, 2).
gates1q(c8, 1).
gates2q(c8, 1).
circuit_computer(c8, simulator_mps).


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
energy_cost(M, C, S, Energy_cost) :- dispatch(M,C,S), shots(S), technology(M, superconductor), gates1q(C,G1), gates2q(C,G2), gates1q_speed(M,G1_speed), gates2q_speed(M,G2_speed), kWh(M, K), circuit_depth(C, Req_depth), Energy_cost = S*(G1_speed*G1 + G2_speed*G2)*K.
energy_cost(M, C, S, Energy_cost) :- dispatch(M,C,S), shots(S), technology(M, trapped_ions), gates1q(C,G1), gates2q(C,G2), gates1q_speed(M,G1_speed), gates2q_speed(M,G2_speed), kWh(M, K), Energy_cost = S*(G1_speed*G1 + G2_speed*G2)*K.
energy_cost(M, C, S, Energy_cost) :- dispatch(M,C,S), shots(S), technology(M, neutral_atoms), gates1q(C,G1), gates2q(C,G2), kWh(M, K), Energy_cost = ((G1 + G2)*S)/1000 * K.
energy_cost(M, C, S, Energy_cost) :- dispatch(M,C,S), shots(S), technology(M, simulator), gates1q(C,G1), gates2q(C,G2), kWh(M, K), Energy_cost = ((G1 + G2)*S)/10000 * K.
#show total_energy_cost/1.

total_shots(20000).
granularity(4000).
european_machines(European_machines) :- European_machines = #sum{ 1, M : dispatch(M, _, S), shots(S), S > 0, region(M, europe) }.
max_cost(99999999).
max_time(99999999).
#show european_machines/1.
