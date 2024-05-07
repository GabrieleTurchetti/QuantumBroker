import math
from .dispatch_utils import get_dispatch_deviation

STANDARD_METRICS = ["total_cost", "total_energy_cost", "total_time", "used_computers", "shots_difference"]

def get_normalized_value(value, min, max):
    return (value - min) / ((max - min) if max != min else 1)

def get_dispatch_value(dispatch, total_shots, metric_weights, min_values, max_values):
    total_value = 0
    
    # Check if the metrics are in the request, then add the partial linear combination for each metric to the total value
    if "total_cost" in metric_weights:
        total_cost = list(dispatch["total_cost"])[0][0]
        normalized_total_cost = get_normalized_value(total_cost, min_values["total_cost"], max_values["total_cost"])
        total_value += metric_weights["total_cost"] * normalized_total_cost

    if "total_energy_cost" in metric_weights:
        total_energy_cost = list(dispatch["total_energy_cost"])[0][0]
        normalized_total_energy_cost = get_normalized_value(total_energy_cost, min_values["total_energy_cost"], max_values["total_energy_cost"])
        total_value += metric_weights["total_energy_cost"] * normalized_total_energy_cost
        
    if "total_time" in metric_weights:
        total_time = list(dispatch["total_time"])[0][0]
        normalized_total_time = get_normalized_value(total_time, min_values["total_time"], max_values["total_time"])
        total_value += metric_weights["total_time"] * normalized_total_time
        
    if "used_computers" in metric_weights:
        used_computers = len(dispatch["dispatch"])
        normalized_used_computers = get_normalized_value(used_computers, min_values["used_computers"], max_values["used_computers"])
        total_value += metric_weights["used_computers"] * normalized_used_computers
        
    if "shots_difference" in metric_weights:
        shots_difference = get_dispatch_deviation(dispatch, total_shots)
        normalized_shots_difference = get_normalized_value(shots_difference, min_values["shots_difference"], max_values["shots_difference"])
        total_value += metric_weights["shots_difference"] * normalized_shots_difference

    # Same job above, but for each custom metric
    for key, value in metric_weights.items():
        if not key in STANDARD_METRICS:
            metric_value = list(dispatch[key])[0][0]
            normalized_metric_value = get_normalized_value(metric_value, min_values[key], max_values[key])
            total_value += value * normalized_metric_value

    return total_value

def filter_dispatches_by_custom_policy(dispatches, total_shots, metric_weights, level):
    # Get the min and max values of each metric in the request, that are later used for calculate the normalized metric values
    min_total_cost = list(min(dispatches, key = lambda dispatch: list(dispatch["total_cost"])[0][0])["total_cost"])[0][0] if "total_cost" in metric_weights else 0
    max_total_cost = list(max(dispatches, key = lambda dispatch: list(dispatch["total_cost"])[0][0])["total_cost"])[0][0] if "total_cost" in metric_weights else 0
    min_total_energy_cost = list(min(dispatches, key = lambda dispatch: list(dispatch["total_energy_cost"])[0][0])["total_energy_cost"])[0][0] if "total_energy_cost" in metric_weights else 0
    max_total_energy_cost = list(max(dispatches, key = lambda dispatch: list(dispatch["total_energy_cost"])[0][0])["total_energy_cost"])[0][0] if "total_energy_cost" in metric_weights else 0
    min_total_time = list(min(dispatches, key = lambda dispatch: list(dispatch["total_time"])[0][0])["total_time"])[0][0] if "total_time" in metric_weights else 0
    max_total_time = list(max(dispatches, key = lambda dispatch: list(dispatch["total_time"])[0][0])["total_time"])[0][0] if "total_time" in metric_weights else 0
    min_used_computers = len(min(dispatches, key = lambda dispatch: len(dispatch["dispatch"]))["dispatch"]) if "used_computers" in metric_weights else 0
    max_used_computers = len(max(dispatches, key = lambda dispatch: len(dispatch["dispatch"]))["dispatch"]) if "used_computers" in metric_weights else 0
    min_shots_difference = get_dispatch_deviation(min(dispatches, key = lambda dispatch: get_dispatch_deviation(dispatch, total_shots)), total_shots) if "shots_difference" in metric_weights else 0
    max_shots_difference = get_dispatch_deviation(max(dispatches, key = lambda dispatch: get_dispatch_deviation(dispatch, total_shots)), total_shots) if "shots_difference" in metric_weights else 0
    additional_min_values = {}
    additional_max_values = {}

    # Same job above, but for each custom metric
    for key in metric_weights.keys():
        if not key in STANDARD_METRICS:
            try:
                additional_min_values[key] = list(min(dispatches, key = lambda dispatch: list(dispatch[key])[0][0])[key])[0][0]
                additional_max_values[key] = list(max(dispatches, key = lambda dispatch: list(dispatch[key])[0][0])[key])[0][0]
            except:
                raise Exception("Metric not found")

    min_values = {
        "total_cost": min_total_cost,
        "total_energy_cost": min_total_energy_cost,
        "total_time": min_total_time,
        "used_computers": min_used_computers,
        "shots_difference": min_shots_difference
    }

    max_values = {
        "total_cost": max_total_cost,
        "total_energy_cost": min_total_energy_cost,
        "total_time": max_total_time,
        "used_computers": max_used_computers,
        "shots_difference": max_shots_difference
    }

    min_values.update(additional_min_values)
    max_values.update(additional_max_values)
    percentage = 100 - level # Percentage of the dispatches than will have to remain
    new_size = math.ceil((len(dispatches) * percentage) / 100) # Size of the new dispatches list
    # Sort the list of the dispatches by the calculated value of each dispatch
    dispatches.sort(key = lambda dispatch: get_dispatch_value(dispatch, total_shots, metric_weights, min_values, max_values), reverse = True)
    return dispatches[:new_size]