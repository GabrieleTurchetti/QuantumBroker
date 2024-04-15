machine(ibm_brisbane).
status(ibm_brisbane, online).
technology(ibm_brisbane, superconductor).
qubits(ibm_brisbane, 127).
language(ibm_brisbane, openqasm2).
kWh(ibm_brisbane, 2).
max_shots(ibm_brisbane, 20000).
max_depth(ibm_brisbane, 100).
expected_waiting_time(ibm_brisbane, 0).
expected_execution_time(ibm_brisbane, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*10*S/10.
expected_cost(ibm_brisbane, C, Res) :- dispatch(ibm_brisbane, C, Dispatch), Res = 6*Dispatch/100.
region(ibm_brisbane, australia).
gates1q_speed(ibm_brisbane, 20).
gates2q_speed(ibm_brisbane, 200).

machine(ibm_osaka).
status(ibm_osaka, online).
technology(ibm_osaka, superconductor).
language(ibm_osaka, openqasm2).
qubits(ibm_osaka, 127).
kWh(ibm_osaka, 1).
max_shots(ibm_osaka, 20000).
max_depth(ibm_osaka, 100).
expected_waiting_time(ibm_osaka, 0).
expected_execution_time(ibm_osaka, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*9*S/10.
expected_cost(ibm_osaka, C, Res) :- dispatch(ibm_osaka, C, Dispatch), Res = 5*Dispatch/100.
region(ibm_osaka, asia).
gates1q_speed(ibm_osaka, 30).
gates2q_speed(ibm_osaka, 300).

machine(simulator_mps).
status(simulator_mps, online).
technology(simulator_mps, simulator).
language(simulator_mps, openqasm2).
qubits(simulator_mps, 100).
max_depth(simulator_mps, 100).
max_shots(simulator_mps, 20000).
kWh(simulator_mps, 6).
expected_waiting_time(simulator_mps, 0).
expected_execution_time(simulator_mps, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*8*S/10.
expected_cost(simulator_mps, C, Res) :- dispatch(simulator_mps, C, Dispatch), Res = 4*Dispatch/100.
region(simulator_mps, europe).
region(simulator_mps, north_america).
region(simulator_mps, south_america).
region(simulator_mps, asia).
region(simulator_mps, africa).
region(simulator_mps, australia).
gates1q_speed(simulator_mps, 40).
gates2q_speed(simulator_mps, 400).

machine(simulator_extended_stabilizer).
status(simulator_extended_stabilizer, online).
technology(simulator_extended_stabilizer, simulator).
language(simulator_extended_stabilizer, openqasm2).
qubits(simulator_extended_stabilizer, 63).
max_depth(simulator_extended_stabilizer, 100).
max_shots(simulator_extended_stabilizer, 20000).
kWh(simulator_extended_stabilizer, 5).
expected_waiting_time(simulator_extended_stabilizer, 0).
expected_execution_time(simulator_extended_stabilizer, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*7*S/10.
expected_cost(simulator_extended_stabilizer, C, Res) :- dispatch(simulator_extended_stabilizer, C, Dispatch), Res = 3*Dispatch/100.
region(simulator_extended_stabilizer, europe).
region(simulator_extended_stabilizer, north_america).
region(simulator_extended_stabilizer, south_america).
region(simulator_extended_stabilizer, asia).
region(simulator_extended_stabilizer, africa).
region(simulator_extended_stabilizer, australia).
gates1q_speed(simulator_extended_stabilizer, 50).
gates2q_speed(simulator_extended_stabilizer, 500).

machine(ibmq_qasm_simulator).
status(ibmq_qasm_simulator, online).
technology(ibmq_qasm_simulator, simulator).
language(ibmq_qasm_simulator, openqasm2).
qubits(ibmq_qasm_simulator, 32).
max_depth(ibmq_qasm_simulator, 100).
max_shots(ibmq_qasm_simulator, 20000).
kWh(ibmq_qasm_simulator, 4).
expected_waiting_time(ibmq_qasm_simulator, 0).
expected_execution_time(ibmq_qasm_simulator, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*6*S/10.
expected_cost(ibmq_qasm_simulator, C, Res) :- dispatch(ibmq_qasm_simulator, C, Dispatch), Res = 2*Dispatch/100.
region(ibmq_qasm_simulator, europe).
region(ibmq_qasm_simulator, north_america).
region(ibmq_qasm_simulator, south_america).
region(ibmq_qasm_simulator, asia).
region(ibmq_qasm_simulator, africa).
region(ibmq_qasm_simulator, australia).
gates1q_speed(ibmq_qasm_simulator, 60).
gates2q_speed(ibmq_qasm_simulator, 600).

machine(simulator_statevector).
status(simulator_statevector, online).
technology(simulator_statevector, simulator).
language(simulator_statevector, openqasm2).
qubits(simulator_statevector, 32).
max_depth(simulator_statevector, 100).
max_shots(simulator_statevector, 20000).
kWh(simulator_statevector, 3).
expected_waiting_time(simulator_statevector, 0).
expected_execution_time(simulator_statevector, C, S, Res) :- circuit_depth(C, Req_depth), shots(S), Res = Req_depth*5*S/10.
expected_cost(simulator_statevector, C, Res) :- dispatch(simulator_statevector, C, Dispatch), Res = 1*Dispatch/100.
region(simulator_statevector, europe).
region(simulator_statevector, north_america).
region(simulator_statevector, south_america).
region(simulator_statevector, asia).
region(simulator_statevector, africa).
region(simulator_statevector, australia).
gates1q_speed(simulator_statevector, 70).
gates2q_speed(simulator_statevector, 700).
circuit(c1).
circuit_depth(c1, 1).
circuit_lang(c1, openqasm2).
circuit_qubits(c1, 48).
gates1q(c1, 9).
gates2q(c1, 1).
circuit_computer(c1, ibm_kyoto).

circuit(c2).
circuit_depth(c2, 1).
circuit_lang(c2, openqasm2).
circuit_qubits(c2, 109).
gates1q(c2, 9).
gates2q(c2, 1).
circuit_computer(c2, ibm_osaka).

circuit(c3).
circuit_depth(c3, 1).
circuit_lang(c3, openqasm2).
circuit_qubits(c3, 2).
gates1q(c3, 3).
gates2q(c3, 1).
circuit_computer(c3, ibmq_qasm_simulator).

circuit(c4).
circuit_depth(c4, 1).
circuit_lang(c4, openqasm2).
circuit_qubits(c4, 2).
gates1q(c4, 1).
gates2q(c4, 1).
circuit_computer(c4, simulator_extended_stabilizer).

circuit(c5).
circuit_depth(c5, 1).
circuit_lang(c5, openqasm2).
circuit_qubits(c5, 2).
gates1q(c5, 1).
gates2q(c5, 1).
circuit_computer(c5, simulator_mps).

circuit(c6).
circuit_depth(c6, 1).
circuit_lang(c6, openqasm2).
circuit_qubits(c6, 2).
gates1q(c6, 3).
gates2q(c6, 1).
circuit_computer(c6, simulator_statevector).

circuit(c7).
circuit_depth(c7, 1).
circuit_lang(c7, openqasm2).
circuit_qubits(c7, 2).
gates1q(c7, 1).
gates2q(c7, 1).
circuit_computer(c7, simulator_stabilizer).

circuit(c8).
circuit_depth(c8, 1).
circuit_lang(c8, openqasm2).
circuit_qubits(c8, 5).
gates1q(c8, 9).
gates2q(c8, 1).
circuit_computer(c8, ibm_brisbane).


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
energy_cost(M, C, S, Energy_cost) :- dispatch(M,C,S), shots(S), technology(M, superconductor), gates1q(C,G1), gates2q(C,G2), gates1q_speed(M,G1_speed), gates2q_speed(M,G2_speed), kWh(M, K), Energy_cost = S*(G1_speed*G1 + G2_speed*G2)*K/1000000.
energy_cost(M, C, S, Energy_cost) :- dispatch(M,C,S), shots(S), technology(M, trapped_ions), gates1q(C,G1), gates2q(C,G2), gates1q_speed(M,G1_speed), gates2q_speed(M,G2_speed), kWh(M, K), Energy_cost = S*(G1_speed*G1 + G2_speed*G2)*K/1000000.
energy_cost(M, C, S, Energy_cost) :- dispatch(M,C,S), shots(S), technology(M, neutral_atoms), gates1q(C,G1), gates2q(C,G2), gates1q_speed(M,G1_speed), gates2q_speed(M,G2_speed), kWh(M, K), Energy_cost = S*(G1_speed*G1 + G2_speed*G2)*K/1000000.
energy_cost(M, C, S, Energy_cost) :- dispatch(M,C,S), shots(S), technology(M, simulator), gates1q(C,G1), gates2q(C,G2), gates1q_speed(M,G1_speed), gates2q_speed(M,G2_speed), kWh(M, K), Energy_cost = S*(G1_speed*G1 + G2_speed*G2)*K/1000000.
#show total_energy_cost/1.

total_shots(10000).
granularity(2000).
max_cost(99999999).
max_time(99999999).
