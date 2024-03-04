import math

def get_dispatch_standard_deviation(dispatch, total_shots):
    avg = total_shots / len(dispatch["dispatch"])
    sum = 0

    for _, _, shots in dispatch["dispatch"]:
        sum += (shots - avg) ** 2

    deviation = math.sqrt(sum / len(dispatch["dispatch"]))
    return deviation

def get_dispatch_value(dispatch, total_shots, weights, min_values, max_values):
    cost_weight, time_weight, reliability_weight, uniformity_weight = weights
    cost = list(dispatch["total_cost"])[0][0]
    time = list(dispatch["total_time"])[0][0]
    used_computers = len(dispatch["dispatch"])
    deviation = get_dispatch_standard_deviation(dispatch, total_shots)
    normalized_cost = (cost - min_values[0]) / ((max_values[0] - min_values[0]) if (max_values[0] - min_values[0]) != 0 else 1)
    normalized_time = (time - min_values[1]) / ((max_values[1] - min_values[1]) if (max_values[1] - min_values[1]) != 0 else 1)
    normalized_used_computers = (used_computers - min_values[2]) / ((max_values[2] - min_values[2]) if (max_values[2] - min_values[2]) != 0 else 1)
    normalized_deviation = (deviation - min_values[3]) / ((max_values[3] - min_values[3]) if (max_values[3] - min_values[3]) != 0 else 1)
    value = - normalized_cost * cost_weight - normalized_time * time_weight + normalized_used_computers * reliability_weight - normalized_deviation * uniformity_weight
    return value

def filter_dispatches_by_policy(dispatches, total_shots, weights, level):
    min_cost = list(min(dispatches, key = lambda dispatch: list(dispatch["total_cost"])[0][0])["total_cost"])[0][0]
    min_time = list(min(dispatches, key = lambda dispatch: list(dispatch["total_time"])[0][0])["total_time"])[0][0]
    min_used_computers = len(min(dispatches, key = lambda dispatch: len(dispatch["dispatch"]))["dispatch"])
    min_deviation = get_dispatch_standard_deviation(min(dispatches, key = lambda dispatch: get_dispatch_standard_deviation(dispatch, total_shots)), total_shots)
    max_cost = list(max(dispatches, key = lambda dispatch: list(dispatch["total_cost"])[0][0])["total_cost"])[0][0]
    max_time = list(max(dispatches, key = lambda dispatch: list(dispatch["total_time"])[0][0])["total_time"])[0][0]
    max_used_computers = len(max(dispatches, key = lambda dispatch: len(dispatch["dispatch"]))["dispatch"])
    max_deviation = get_dispatch_standard_deviation(max(dispatches, key = lambda dispatch: get_dispatch_standard_deviation(dispatch, total_shots)), total_shots)
    min_values = (min_cost, min_time, min_used_computers, min_deviation)
    max_values = (max_cost, max_time, max_used_computers, max_deviation)
    percentage = 100 - level
    new_size = math.ceil((len(dispatches) * percentage) / 100)
    dispatches.sort(key = lambda dispatch: get_dispatch_value(dispatch, total_shots, weights, min_values, max_values), reverse = True)
    return dispatches[:new_size]