import math
from .distribution_utils import get_dispatch_mean_deviation
from .custom_policy import filter_dispatches_by_custom_policy

# Cost-aware policy
def filter_dispatches_by_cost_aware_policy(dispatches, total_shots, level):
    return filter_dispatches_by_custom_policy(dispatches, total_shots, {
        "total_cost": -1,
    }, level)

# Time-aware policy
def filter_dispatches_by_time_aware_policy(dispatches, total_shots, level):
    return filter_dispatches_by_custom_policy(dispatches, total_shots, {
        "total_time": -1,
    }, level)

def get_dispatch_reliability(dispatch, total_shots):
    used_computers = len(dispatch["dispatch"])
    shots_difference = get_dispatch_mean_deviation(dispatch, total_shots)
    avg = total_shots / used_computers
    reliability = used_computers / (shots_difference / avg + 1)
    return reliability

# Reliable policy
def filter_dispatches_by_reliable_policy(dispatches, total_shots, level):
    percentage = 100 - level # Percentage of the dispatches than will have to remain
    new_size = math.ceil((len(dispatches) * percentage) / 100) # Size of the new dispatches list
    # Sort the list of the dispatches by the calculated value of each dispatch
    dispatches.sort(key = lambda dispatch: get_dispatch_reliability(dispatch, total_shots), reverse = True)
    return dispatches[:new_size]
    
# Green policy
def filter_dispatches_by_green_policy(dispatches, total_shots, level):
    return filter_dispatches_by_custom_policy(dispatches, total_shots, {
        "total_energy_cost": -1,
    }, level)
    