import math
from .dispatch_utils import get_dispatch_mean_deviation, get_metric_mean, get_metric_standard_deviation

STANDARD_METRICS = ["total_cost", "total_energy_cost", "total_time", "used_computers", "shots_difference"]

def get_normalized_value(value, mean, standard_deviation):
    return (value - mean) / (standard_deviation if standard_deviation != 0 else 1)

def get_dispatch_value(dispatch, total_shots, metric_weights, mean_values, standard_deviation_values):
    total_value = 0
    
    # Check if the metrics are in the request, then add the partial linear combination for each metric to the total value
    if "total_cost" in metric_weights:
        total_cost = list(dispatch["total_cost"])[0][0]
        normalized_total_cost = get_normalized_value(total_cost, mean_values["total_cost"], standard_deviation_values["total_cost"])
        total_value += metric_weights["total_cost"] * normalized_total_cost

    if "total_energy_cost" in metric_weights:
        total_energy_cost = list(dispatch["total_energy_cost"])[0][0]
        normalized_total_energy_cost = get_normalized_value(total_energy_cost, mean_values["total_energy_cost"], standard_deviation_values["total_energy_cost"])
        total_value += metric_weights["total_energy_cost"] * normalized_total_energy_cost
        
    if "total_time" in metric_weights:
        total_time = list(dispatch["total_time"])[0][0]
        normalized_total_time = get_normalized_value(total_time, mean_values["total_time"], standard_deviation_values["total_time"])
        total_value += metric_weights["total_time"] * normalized_total_time
        
    if "used_computers" in metric_weights:
        used_computers = len(dispatch["dispatch"])
        normalized_used_computers = get_normalized_value(used_computers, mean_values["used_computers"], standard_deviation_values["used_computers"])
        total_value += metric_weights["used_computers"] * normalized_used_computers
        
    if "shots_difference" in metric_weights:
        shots_difference = get_dispatch_mean_deviation(dispatch, total_shots)
        normalized_shots_difference = get_normalized_value(shots_difference, mean_values["shots_difference"], standard_deviation_values["shots_difference"])
        total_value += metric_weights["shots_difference"] * normalized_shots_difference

    # Same job above, but for each custom metric
    for key, value in metric_weights.items():
        if not key in STANDARD_METRICS:
            metric_value = list(dispatch[key])[0][0]
            normalized_metric_value = get_normalized_value(metric_value, mean_values[key], standard_deviation_values[key])
            total_value += value * normalized_metric_value

    return total_value

def filter_dispatches_by_custom_policy(dispatches, total_shots, metric_weights, level):
    # Get the mean and the standard deviation values of each metric in the request, that are later used for calculate the normalized metric values
    mean_total_cost = get_metric_mean(list(map(lambda dispatch: list(dispatch["total_cost"])[0][0], dispatches))) if "total_cost" in metric_weights else 0
    mean_total_energy_cost = get_metric_mean(list(map(lambda dispatch: list(dispatch["total_energy_cost"])[0][0], dispatches))) if "total_energy_cost" in metric_weights else 0
    mean_total_time = get_metric_mean(list(map(lambda dispatch: list(dispatch["total_time"])[0][0], dispatches))) if "total_time" in metric_weights else 0
    mean_used_computers = get_metric_mean(list(map(lambda dispatch: len(dispatch["dispatch"]), dispatches))) if "used_computers" in metric_weights else 0
    mean_shots_difference = get_metric_mean(list(map(lambda dispatch: get_dispatch_mean_deviation(dispatch, total_shots), dispatches))) if "shots_difference" in metric_weights else 0
    
    standard_deviation_total_cost = get_metric_standard_deviation(list(map(lambda dispatch: list(dispatch["total_cost"])[0][0], dispatches))) if "total_cost" in metric_weights else 0
    standard_deviation_total_energy_cost = get_metric_standard_deviation(list(map(lambda dispatch: list(dispatch["total_energy_cost"])[0][0], dispatches))) if "total_energy_cost" in metric_weights else 0
    standard_deviation_used_computers = get_metric_standard_deviation(list(map(lambda dispatch: len(dispatch["dispatch"]), dispatches))) if "used_computers" in metric_weights else 0
    standard_deviation_total_time = get_metric_standard_deviation(list(map(lambda dispatch: list(dispatch["total_time"])[0][0], dispatches))) if "total_time" in metric_weights else 0
    standard_deviation_shots_difference = get_metric_standard_deviation(list(map(lambda dispatch: get_dispatch_mean_deviation(dispatch, total_shots), dispatches))) if "shots_difference" in metric_weights else 0
    
    additional_mean_values = {}
    additional_standard_deviation_values = {}

    # Same job above, but for each custom metric
    for key in metric_weights.keys():
        if not key in STANDARD_METRICS:
            try:
                additional_mean_values[key] = get_metric_mean(list(map(lambda dispatch: list(dispatch[key])[0][0], dispatches)))
                additional_standard_deviation_values[key] = get_metric_standard_deviation(list(map(lambda dispatch: list(dispatch[key])[0][0], dispatches)))
            except:
                raise Exception("Metric not found")

    mean_values = {
        "total_cost": mean_total_cost,
        "total_energy_cost": mean_total_energy_cost,
        "total_time": mean_total_time,
        "used_computers": mean_used_computers,
        "shots_difference": mean_shots_difference
    }

    standard_deviation_values = {
        "total_cost": standard_deviation_total_cost,
        "total_energy_cost": mean_total_energy_cost,
        "total_time": standard_deviation_total_time,
        "used_computers": standard_deviation_used_computers,
        "shots_difference": standard_deviation_shots_difference
    }

    mean_values.update(additional_mean_values)
    standard_deviation_values.update(additional_standard_deviation_values)
    percentage = 100 - level # Percentage of the dispatches than will have to remain
    new_size = math.ceil((len(dispatches) * percentage) / 100) # Size of the new dispatches list
    # Sort the list of the dispatches by the calculated value of each dispatch
    dispatches.sort(key = lambda dispatch: get_dispatch_value(dispatch, total_shots, metric_weights, mean_values, standard_deviation_values), reverse = True)
    return dispatches[:new_size]