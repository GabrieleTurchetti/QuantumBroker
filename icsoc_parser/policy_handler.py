import math

def get_dispatch_standard_deviation(dispatch, total_shots):
    avg = total_shots / len(dispatch["dispatch"])
    sum = 0

    for _, _, shots in dispatch["dispatch"]:
        sum += (shots - avg) ** 2

    deviation = math.sqrt(sum / len(dispatch["dispatch"]))
    return deviation

def get_dispatch_used_computers(dispatch):
    length = 0

    for _, _, shots in dispatch["dispatch"]:
        if shots != 0:
            length += 1

    return length

def get_dispatch_value(dispatch, total_shots, weights, min_values, max_values):
    cost = list(dispatch["total_cost"])[0][0]
    energy_cost = list(dispatch["total_energy_cost"])[0][0]
    time = list(dispatch["total_time"])[0][0]
    used_computers = get_dispatch_used_computers(dispatch)
    deviation = get_dispatch_standard_deviation(dispatch, total_shots)
    normalized_cost = (cost - min_values["cost"]) / ((max_values["cost"] - min_values["cost"]) if (max_values["cost"] - min_values["cost"]) != 0 else 1)
    normalized_energy_cost = (energy_cost - min_values["energy_cost"]) / ((max_values["energy_cost"] - min_values["energy_cost"]) if (max_values["energy_cost"] - min_values["energy_cost"]) != 0 else 1)
    normalized_time = (time - min_values["time"]) / ((max_values["time"] - min_values["time"]) if (max_values["time"] - min_values["time"]) != 0 else 1)
    normalized_used_computers = (used_computers - min_values["used_computers"]) / ((max_values["used_computers"] - min_values["used_computers"]) if (max_values["used_computers"] - min_values["used_computers"]) != 0 else 1)
    normalized_deviation = (deviation - min_values["deviation"]) / ((max_values["deviation"] - min_values["deviation"]) if (max_values["deviation"] - min_values["deviation"]) != 0 else 1)
    value = - normalized_cost * weights["cost"] - normalized_energy_cost * weights["eco_sustainability"] - normalized_time * weights["time"] + normalized_used_computers * weights["reliability"] - normalized_deviation * weights["uniformity"]
    return value

def filter_dispatches_by_policy(dispatches, total_shots, weights, level):
    min_cost = list(min(dispatches, key = lambda dispatch: list(dispatch["total_cost"])[0][0])["total_cost"])[0][0]
    min_energy_cost = list(min(dispatches, key = lambda dispatch: list(dispatch["total_energy_cost"])[0][0])["total_energy_cost"])[0][0]
    min_time = list(min(dispatches, key = lambda dispatch: list(dispatch["total_time"])[0][0])["total_time"])[0][0]
    min_used_computers = get_dispatch_used_computers(min(dispatches, key = lambda dispatch: len(dispatch["dispatch"])))
    min_deviation = get_dispatch_standard_deviation(min(dispatches, key = lambda dispatch: get_dispatch_standard_deviation(dispatch, total_shots)), total_shots)
    max_cost = list(max(dispatches, key = lambda dispatch: list(dispatch["total_cost"])[0][0])["total_cost"])[0][0]
    max_energy_cost = list(max(dispatches, key = lambda dispatch: list(dispatch["total_energy_cost"])[0][0])["total_energy_cost"])[0][0]
    max_time = list(max(dispatches, key = lambda dispatch: list(dispatch["total_time"])[0][0])["total_time"])[0][0]
    max_used_computers = get_dispatch_used_computers(max(dispatches, key = lambda dispatch: len(dispatch["dispatch"])))
    max_deviation = get_dispatch_standard_deviation(max(dispatches, key = lambda dispatch: get_dispatch_standard_deviation(dispatch, total_shots)), total_shots)

    min_values = {
        "cost": min_cost,
        "energy_cost": min_energy_cost,
        "time": min_time,
        "used_computers": min_used_computers,
        "deviation": min_deviation
    }

    max_values = {
        "cost": max_cost,
        "energy_cost": max_energy_cost,
        "time": max_time,
        "used_computers": max_used_computers,
        "deviation": max_deviation
    }
    
    percentage = 100 - level
    new_size = math.ceil((len(dispatches) * percentage) / 100)
    dispatches.sort(key = lambda dispatch: get_dispatch_value(dispatch, total_shots, weights, min_values, max_values), reverse = True)
    return dispatches[:new_size]