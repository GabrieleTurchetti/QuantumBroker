import math

STANDARD_METRIC_NAMES = ["total_cost", "total_time", "used_computers", "shots_difference"]

def get_dispatch_deviation(dispatch, total_shots):
    avg = total_shots / get_dispatch_len(dispatch)
    sum = 0

    for _, _, shots in dispatch["dispatch"]:
        if shots != 0:
            sum += abs(shots - avg)

    deviation = sum / get_dispatch_len(dispatch)
    return deviation

def get_dispatch_len(dispatch):
    length = 0

    for _, _, shots in dispatch["dispatch"]:
        if shots != 0:
            length += 1

    return length

def get_dispatch_value(dispatch, total_shots, weights, min_values, max_values):
    total_cost = list(dispatch["total_cost"])[0][0]
    total_time = list(dispatch["total_time"])[0][0]
    used_computers = get_dispatch_len(dispatch)
    shots_difference = get_dispatch_deviation(dispatch, total_shots)
    normalized_total_cost = (total_cost - min_values["total_cost"]) / ((max_values["total_cost"] - min_values["total_cost"]) if (max_values["total_cost"] - min_values["total_cost"]) != 0 else 1)
    normalized_total_time = (total_time - min_values["total_time"]) / ((max_values["total_time"] - min_values["total_time"]) if (max_values["total_time"] - min_values["total_time"]) != 0 else 1)
    normalized_used_computers = (used_computers - min_values["used_computers"]) / ((max_values["used_computers"] - min_values["used_computers"]) if (max_values["used_computers"] - min_values["used_computers"]) != 0 else 1)
    normalized_shots_difference = (shots_difference - min_values["shots_difference"]) / ((max_values["shots_difference"] - min_values["shots_difference"]) if (max_values["shots_difference"] - min_values["shots_difference"]) != 0 else 1)
    value = normalized_total_cost * (weights["total_cost"] if "total_cost" in weights else 0) + normalized_total_time * (weights["total_time"] if "total_time" in weights else 0) + normalized_used_computers * (weights["used_computers"] if "used_computers" in weights else 0) + normalized_shots_difference * (weights["shots_difference"] if "shots_difference" in weights else 0)

    for key, _ in weights.items():
        if not key in STANDARD_METRIC_NAMES:
            addional_value = list(dispatch[key])[0][0]
            additional_normalized_value = (addional_value - min_values[key]) / ((max_values[key] - min_values[key]) if (max_values[key] - min_values[key]) != 0 else 1)
            value += additional_normalized_value * weights[key]

    return value

def filter_dispatches_by_policy(dispatches, total_shots, weights, level):
    min_total_cost = list(min(dispatches, key = lambda dispatch: list(dispatch["total_cost"])[0][0])["total_cost"])[0][0] if "total_cost" in weights else 0
    max_total_cost = list(max(dispatches, key = lambda dispatch: list(dispatch["total_cost"])[0][0])["total_cost"])[0][0] if "total_cost" in weights else 0
    min_total_time = list(min(dispatches, key = lambda dispatch: list(dispatch["total_time"])[0][0])["total_time"])[0][0] if "total_time" in weights else 0
    max_total_time = list(max(dispatches, key = lambda dispatch: list(dispatch["total_time"])[0][0])["total_time"])[0][0] if "total_time" in weights else 0
    min_used_computers = get_dispatch_len(min(dispatches, key = lambda dispatch: get_dispatch_len(dispatch))) if "used_computers" in weights else 0
    max_used_computers = get_dispatch_len(max(dispatches, key = lambda dispatch: get_dispatch_len(dispatch))) if "used_computers" in weights else 0
    min_shots_difference = get_dispatch_deviation(min(dispatches, key = lambda dispatch: get_dispatch_deviation(dispatch, total_shots)), total_shots) if "shots_difference" in weights else 0
    max_shots_difference = get_dispatch_deviation(max(dispatches, key = lambda dispatch: get_dispatch_deviation(dispatch, total_shots)), total_shots) if "shots_difference" in weights else 0
    additional_min_values = {}
    additional_max_values = {}

    for key, _ in weights.items():
        if not key in STANDARD_METRIC_NAMES:
            try:
                additional_min_values[key] = list(min(dispatches, key = lambda dispatch: list(dispatch[key])[0][0])[key])[0][0]
                additional_max_values[key] = list(max(dispatches, key = lambda dispatch: list(dispatch[key])[0][0])[key])[0][0]
            except:
                raise Exception("Metric name not found")

    min_values = {
        "total_cost": min_total_cost,
        "total_time": min_total_time,
        "used_computers": min_used_computers,
        "shots_difference": min_shots_difference
    }

    max_values = {
        "total_cost": max_total_cost,
        "total_time": max_total_time,
        "used_computers": max_used_computers,
        "shots_difference": max_shots_difference
    }

    min_values.update(additional_min_values)
    max_values.update(additional_max_values)
    percentage = 100 - level
    new_size = math.ceil((len(dispatches) * percentage) / 100)
    dispatches.sort(key = lambda dispatch: get_dispatch_value(dispatch, total_shots, weights, min_values, max_values), reverse = True)
    return dispatches[:new_size]