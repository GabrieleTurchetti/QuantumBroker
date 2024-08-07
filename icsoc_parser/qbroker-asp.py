import json
import time

from datetime import datetime
from clyngor import solve

from asp.machine_parser import parse_machines
from asp.request_parser import parse_request
from asp.circuit_parser import parse_circuit
from qbroker import QBroker

from distribution.distribution_manager import filter_dispatches_by_policies

CONFIG = "../config.json"

def _parse_request(request):
    OUTPUT = "asp/"+"request.lp"
    DEFAULT = "asp/"+"default.lp"
    
    print("Parsing request {}...".format(REQUEST))

    with open(REQUEST) as f:
        request = json.load(f)

    parsed_request = parse_request(request)

    with open(DEFAULT) as f:
        default = f.read()

    parsed_request = default + "\n\n" + parsed_request

    with open(OUTPUT, "w+") as f:
        f.write(parsed_request)
        # print(parsed_request)

def _parse_computers(computers):
    MAP = "asp/"+"machines-map.json"
    OUTPUT = "asp/"+"machines.lp"

    with open(MAP) as f:
        machines_map = json.load(f)

    parsed_machines = parse_machines(computers, machines_map)

    with open(OUTPUT, "w+") as f:
        f.write("\n".join(parsed_machines))

def _parse_circuit(circuit):
    OUTPUT = "asp/circuits.lp"
    parsed_circuit = parse_circuit(circuit)

    with open(OUTPUT, "w+") as f:
        f.write(parsed_circuit)

def policy(computers, original_request):
    # _parse_computers(computers)
    _parse_request(original_request)
    # _parse_circuit(original_request["circuit"])

    with open("asp/"+"request.lp") as f:
        request = f.read()

    with open("asp/"+"circuits.lp") as f:
        circuits = f.read()

    with open("asp/"+"machines.lp") as f:
        machines = f.read()

    with open("asp/"+"program.lp", "w+") as f:
        f.write(machines)
        f.write("\n")
        f.write(circuits)
        f.write("\n")
        f.write(request)

    # print("Solving...")
    start = time.time()
    print("Start time: {}".format(datetime.fromtimestamp(start)))

    if "@time_limit" in original_request:
        answers = solve("asp/"+'program.lp', options=["--time-limit={}".format(original_request["@time_limit"])])
    else:
        answers = solve("asp/"+'program.lp') 

    dispatches = []

    for answer in answers.by_predicate:
        dispatches.append(answer)
    
    print("")
    print(*dispatches, sep = "\n\n")    
    answer = filter_dispatches_by_policies(dispatches, original_request["shots"], original_request["distribution_policies"])
    end = time.time()
    # print("End time: {}".format(datetime.fromtimestamp(end)))
    print("\nTime elapsed: {}".format(end - start))
    print(f"\nDispatch selected: {answer}\n")
    return parse_answer(answer)

def parse_answer(answer):
    return answer["dispatch"]

def print_results(results):
    for result in results:
        print(f"\n{result}")

REQUEST = ""

with open(CONFIG, "r") as f:
    REQUEST = json.load(f)["request_path"]

if __name__ == "__main__":
    qb = QBroker(policy)
    # print(qb)

    with open(REQUEST) as f:
        original_request = json.load(f)
    
    print(qb.run(original_request))