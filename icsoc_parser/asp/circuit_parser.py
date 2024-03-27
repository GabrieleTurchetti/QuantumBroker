import sys

sys.path.append("../")

from src.components.qbroker import brokering
from src.qbroker_asp import parse_circuit as parse

def parse_circuit(circuit):
    circuits = brokering(circuit)
    circuits_parsed = ""
    i = 1

    for circuit in circuits.items():
        circuit_parsed = parse(f"c{i}", circuit[1])
        circuits_parsed += circuit_parsed
        i += 1

    return circuits_parsed