import math
from .dispatch_utils import get_dispatch_len, get_dispatch_deviation

STANDARD_METRICS = ["total_cost", "total_energy_cost", "total_time", "used_computers", "shots_difference"]

def normalized_value(value, min, max):
    return (value - min) / ((max - min) if max != min else 1)

def get_dispatch_value(dispatch, total_shots, metrics, min_values, max_values):
    total_cost = list(dispatch["total_cost"])[0][0]
    total_energy_cost = list(dispatch["total_energy_cost"])[0][0]
    total_time = list(dispatch["total_time"])[0][0]
    used_computers = get_dispatch_len(dispatch)
    shots_difference = get_dispatch_deviation(dispatch, total_shots)
    normalized_total_cost = normalized_value(total_cost, min_values["total_cost"], max_values["total_cost"])
    normalized_total_energy_cost = normalized_value(total_energy_cost, min_values["total_energy_cost"], max_values["total_energy_cost"])
    normalized_total_time = normalized_value(total_time, min_values["total_time"], max_values["total_time"])
    normalized_used_computers = normalized_value(used_computers, min_values["used_computers"], max_values["used_computers"])
    normalized_shots_difference = normalized_value(shots_difference, min_values["shots_difference"], max_values["shots_difference"])
    value = normalized_total_cost * (metrics["total_cost"] if "total_cost" in metrics else 0) + \
        normalized_total_energy_cost * (metrics["total_energy_cost"] if "total_energy_cost" in metrics else 0) + \
        normalized_total_time * (metrics["total_time"] if "total_time" in metrics else 0) + \
        normalized_used_computers * (metrics["used_computers"] if "used_computers" in metrics else 0) + \
        normalized_shots_difference * (metrics["shots_difference"] if "shots_difference" in metrics else 0)

    for key, _ in metrics.items():
        if not key in STANDARD_METRICS:
            metric_value = list(dispatch[key])[0][0]
            normalized_metric_value = normalized_value(metric_value, min_values[key], max_values[key])
            value += normalized_metric_value * metrics[key]

    return value

def filter_dispatches_by_custom_policy(dispatches, total_shots, metrics, level):
    min_total_cost = list(min(dispatches, key = lambda dispatch: list(dispatch["total_cost"])[0][0])["total_cost"])[0][0] if "total_cost" in metrics else 0
    max_total_cost = list(max(dispatches, key = lambda dispatch: list(dispatch["total_cost"])[0][0])["total_cost"])[0][0] if "total_cost" in metrics else 0
    min_total_energy_cost = list(min(dispatches, key = lambda dispatch: list(dispatch["total_energy_cost"])[0][0])["total_energy_cost"])[0][0] if "total_energy_cost" in metrics else 0
    max_total_energy_cost = list(max(dispatches, key = lambda dispatch: list(dispatch["total_energy_cost"])[0][0])["total_energy_cost"])[0][0] if "total_energy_cost" in metrics else 0
    min_total_time = list(min(dispatches, key = lambda dispatch: list(dispatch["total_time"])[0][0])["total_time"])[0][0] if "total_time" in metrics else 0
    max_total_time = list(max(dispatches, key = lambda dispatch: list(dispatch["total_time"])[0][0])["total_time"])[0][0] if "total_time" in metrics else 0
    min_used_computers = get_dispatch_len(min(dispatches, key = lambda dispatch: get_dispatch_len(dispatch))) if "used_computers" in metrics else 0
    max_used_computers = get_dispatch_len(max(dispatches, key = lambda dispatch: get_dispatch_len(dispatch))) if "used_computers" in metrics else 0
    min_shots_difference = get_dispatch_deviation(min(dispatches, key = lambda dispatch: get_dispatch_deviation(dispatch, total_shots)), total_shots) if "shots_difference" in metrics else 0
    max_shots_difference = get_dispatch_deviation(max(dispatches, key = lambda dispatch: get_dispatch_deviation(dispatch, total_shots)), total_shots) if "shots_difference" in metrics else 0
    additional_min_values = {}
    additional_max_values = {}

    for key, _ in metrics.items():
        if not key in STANDARD_METRICS:
            try:
                additional_min_values[key] = list(min(dispatches, key = lambda dispatch: list(dispatch[key])[0][0])[key])[0][0]
                additional_max_values[key] = list(max(dispatches, key = lambda dispatch: list(dispatch[key])[0][0])[key])[0][0]
            except:
                raise Exception("Metric name not found")

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
    percentage = 100 - level
    new_size = math.ceil((len(dispatches) * percentage) / 100)
    dispatches.sort(key = lambda dispatch: get_dispatch_value(dispatch, total_shots, metrics, min_values, max_values), reverse = True)
    return dispatches[:new_size]