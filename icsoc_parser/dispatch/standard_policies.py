import math
from .dispatch_utils import get_dispatch_deviation
from .custom_policy import filter_dispatches_by_custom_policy

# cost-aware policy
def filter_dispatches_by_cost_aware_policy(dispatches, total_shots, level):
    return filter_dispatches_by_custom_policy(dispatches, total_shots, {
        "total_cost": ("-", 1),
    }, level)

# time-aware policy
def filter_dispatches_by_time_aware_policy(dispatches, total_shots, level):
    return filter_dispatches_by_custom_policy(dispatches, total_shots, {
        "total_time": ("-", 1),
    }, level)

def get_dispatch_reliability(dispatch, total_shots):
    used_computers = len(dispatch["dispatch"])
    shots_difference = get_dispatch_deviation(dispatch, total_shots)
    avg = total_shots / used_computers
    reliability = used_computers / (shots_difference / avg + 1)
    return reliability

# reliable policy
def filter_dispatches_by_reliable_policy(dispatches, total_shots, level):
    percentage = 100 - level
    new_size = math.ceil((len(dispatches) * percentage) / 100)
    dispatches.sort(key = lambda dispatch: get_dispatch_reliability(dispatch, total_shots), reverse = True)
    return dispatches[:new_size]
    
# green policy
def filter_dispatches_by_green_policy(dispatches, total_shots, level):
    return filter_dispatches_by_custom_policy(dispatches, total_shots, {
        "total_energy_cost": ("-", 1),
    }, level)
    