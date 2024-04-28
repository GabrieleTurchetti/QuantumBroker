import sys
import json

sys.path.append("../")

from src.components.qbroker import brokering
from src.qbroker_asp import parse_circuit as parse

CONFIG = "../config.json"

def parse_circuit(circuit):
    circuits = brokering(circuit)
    save_circuits(circuits)
    circuits_parsed = ""
    i = 1

    for circuit in circuits.items():
        circuit_parsed = parse(f"c{i}", circuit[1])
        circuits_parsed += circuit_parsed
        i += 1

    return circuits_parsed

def save_circuits(circuits):
    circuits_path = ""
    circuits_dict = {}
    i = 1

    with open(CONFIG, "r") as f:
        circuits_path = json.load(f)["circuits_path"]

    for circuit in circuits.items():
        circuits_dict[f"c{i}"] = circuit[1]["circuit"]
        i += 1

    with open(circuits_path, 'w') as f:
        json.dump(circuits_dict, f, indent = 4)
