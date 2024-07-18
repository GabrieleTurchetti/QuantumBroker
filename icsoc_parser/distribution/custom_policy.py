import math
from .distribution_utils import get_metric_mean, get_metric_standard_deviation

def get_normalized_value(value, mean, standard_deviation):
    return (value - mean) / (standard_deviation if standard_deviation != 0 else 1)

def get_dispatch_value(dispatch, total_shots, metric_weights, mean_values, standard_deviation_values):
    total_value = 0
    
    # Add the partial linear combination for each metric to the total value
    for key, value in metric_weights.items():
        metric_value = list(dispatch[key])[0][0]
        normalized_metric_value = get_normalized_value(metric_value, mean_values[key], standard_deviation_values[key])
        total_value += value * normalized_metric_value

    return total_value

def filter_dispatches_by_custom_policy(dispatches, total_shots, metric_weights, level):
    mean_values = {}
    standard_deviation_values = {}

    # Get the mean and the standard deviation values of each metric in the request, that are later used for calculate the normalized metric value
    for key in metric_weights.keys():
        try:
            mean_values[key] = get_metric_mean(list(map(lambda dispatch: list(dispatch[key])[0][0], dispatches)))
            standard_deviation_values[key] = get_metric_standard_deviation(list(map(lambda dispatch: list(dispatch[key])[0][0], dispatches)))
        except:
            raise Exception("Metric not found")

    percentage = 100 - level # Percentage of the dispatches than will have to remain
    new_size = math.ceil((len(dispatches) * percentage) / 100) # Size of the new dispatches list
    # Sort the list of the dispatches by the calculated value of each dispatch
    dispatches.sort(key = lambda dispatch: get_dispatch_value(dispatch, total_shots, metric_weights, mean_values, standard_deviation_values), reverse = True)
    return dispatches[:new_size]