import math
from .dispatch_utils import get_dispatch_len, get_dispatch_deviation
from .custom_policy import filter_dispatches_by_custom_policy

def filter_dispatches_by_cost_aware_policy(dispatches, total_shots, level):
    return filter_dispatches_by_custom_policy(dispatches, total_shots, {
        "total_cost": -1,
        "total_time": 0,
        "used_computers": 0,
        "shots_difference": 0
    }, level)

def filter_dispatches_by_time_aware_policy(dispatches, total_shots, level):
    return filter_dispatches_by_custom_policy(dispatches, total_shots, {
        "total_cost": 0,
        "total_time": -1,
        "used_computers": 0,
        "shots_difference": 0
    }, level)

def get_dispatch_reliability(dispatch, total_shots):
    used_computers = get_dispatch_len(dispatch)
    shots_difference = get_dispatch_deviation(dispatch, total_shots)
    reliability = used_computers / ((shots_difference * used_computers) / total_shots + 1)
    return reliability

def filter_dispatches_by_reliable_policy(dispatches, total_shots, level):
    percentage = 100 - level
    new_size = math.ceil((len(dispatches) * percentage) / 100)
    dispatches.sort(key = lambda dispatch: get_dispatch_reliability(dispatch, total_shots), reverse = True)
    return dispatches[:new_size]
    