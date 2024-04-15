import os
import json
import time
import sys
import qiskit.qasm2

sys.path.append("../")

from icsoc_parser.distribution.distribution_manager import get_distribution
from qukit.components.dispatcher import Dispatch, Dispatcher
from qukit.components.virtual_provider import VirtualProvider
from qukit.components.circuits import Circuit
from pyquil import Program
from pyquil.gates import *
from dotenv import load_dotenv

load_dotenv()

IBM_API_TOKEN = os.getenv("IBM_API_TOKEN")
COMPUTERS = "machines"
PATHS_PATH = "../paths.json"

class QBroker:
    def __init__(self, policy, id=0):
        self.policy = policy
        self.id = id

    def __str__(self):
        return "QBroker: id={0}, policy={1}".format(self.id, self.policy)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.id == other.id and self.policy == other.policy
    
    def get_computers(self):
        computers = []
        for c in os.listdir(COMPUTERS):
            if c.endswith(".json"):
                with open(os.path.join(COMPUTERS, c)) as f:
                    computer = json.load(f)
                    computers.append(computer)

        return computers
    
    def dispatch(self, request):
        computers = self.get_computers()
        return self.policy(computers, request)

    def save_results(self, results, policy):
        results_path = ""

        with open(PATHS_PATH, "r") as f:
            results_path = json.load(f)["results_path"]
        
        results_dict = {
            "results": [],
            "distribution": {}
        }

        for result in results:
            result = result.to_dict()
            result_dict = {}
            result_dict[result["backend"]] = result["data"]
            results_dict["results"].append(result_dict)

        results_dict["distribution"] = get_distribution(results, policy)

        with open(results_path, 'w') as f:
            json.dump(results_dict, f, indent = 4)
    
    def run(self, request):
        # print("Running request: {} on {}".format(request, self))
        computers = self.dispatch(request)

        for c in computers:
            print("Sending {} shots for circuit {} to {}".format(c[2], c[1], c[0]))

        circuits_path = ""
        circuits_dict = {}

        with open(PATHS_PATH, "r") as f:
            circuits_path = json.load(f)["circuits_path"]

        with open(circuits_path, "r") as f:
            circuits_dict = json.load(f)

        dispatch = {
            "IBMQ": {}
        }

        for backend, circuit, shots in computers:
            dispatch["IBMQ"][backend] = [(circuits_dict[circuit], shots)]

        virtual_provider = VirtualProvider({
            "IBMQ": IBM_API_TOKEN
        })

        dispatcher = Dispatcher(virtual_provider)
        dispatch = dispatcher.from_dict(dispatch)
        results = {} # dispatcher.run(dispatch)
        self.save_results(results, request["distribution_policy"])
        return results

if __name__ == "__main__":
    def policy(computers, request):
        res = []
        shots_per_computer = request["shots"] // len(computers)
        for c in computers:
            res.append((c["name"],shots_per_computer))
        last = request["shots"] % len(computers)
        if last > 0:
            res.pop()
            res.append((computers[-1]["name"],shots_per_computer+last))
        return res
    
    qb = QBroker(policy)
    print(qb)
    print(qb.run({"shots":2001}))
    