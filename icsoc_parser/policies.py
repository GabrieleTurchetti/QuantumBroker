def get_deviation(dispatch, total_shots):
    avg = total_shots / len(dispatch["dispatch"])
    dev = 0

    for _, _, shots in dispatch["dispatch"]:
        dev += abs(shots - avg)

    return dev

def get_dispatch_value(dispatch, shots, weights, min_values, max_values):
    cost_weight, time_weight, accuracy_weight, uniformity_weight = weights
    cost = list(dispatch["total_cost"])[0][0]
    time = list(dispatch["total_time"])[0][0]
    used_computers = len(dispatch["dispatch"])
    deviation = get_deviation(dispatch, total_shots)
    normalized_cost = (cost - min_values[0]) / (max_values[0] - min_values[0])
    normalized_time = (cost - min_values[1]) / (max_values[1] - min_values[1])
    normalized_used_computers = (cost - min_values[2]) / (max_values[2] - min_values[3])
    normalized_deviation = (cost - min_values[3]) / (max_values[3] - min_values[3])
    return normalized_cost * cost_weight + normalized_time * time_weight + nomalized_used_computers * accuracy_weight + normalized_deviation * uniformity_weight


def standard(dispatches, shots, weights, level):
    min_cost = min(dispatches, key = lambda dispatch: list(dispatch["total_cost"])[0][0])
    min_time = min(dispatches, key = lambda dispatch: list(dispatch["total_time"])[0][0])
    min_used_computers = min(dispatches, key = lambda dispatch: len(dispatch["dispatch"]))
    min_deviation = min(dispatches, key = lambda dispatch: get_deviation(dispatch, total_shots))
    max_cost = max(dispatches, key = lambda dispatch: list(dispatch["total_cost"])[0][0])
    max_time = max(dispatches, key = lambda dispatch: list(dispatch["total_time"])[0][0])
    max_used_computers = max(dispatches, key = lambda dispatch: len(dispatch["dispatch"]))
    max_deviation = max(dispatches, key = lambda dispatch: get_deviation(dispatch, total_shots))
    min_values = (min_cost, min_time, min_used_computers, min_deviation)
    max_values = (max_cost, max_time, max_used_computers, max_deviation)
    percentage = 100 - level
    new_size = math.ceil((len(dispatches) * percentage) / 100)
    dispatches.sort(key = lambda dispatch: get_dispatch_value(dispatch, shots, weights, min_values, max_values), reverse = True)
    return dispatches[:new_size]