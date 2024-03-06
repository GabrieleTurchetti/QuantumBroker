import math
from generic_policy_handler import filter_dispatches_by_policy, get_dispatch_len, get_dispatch_deviation

def cost_aware(dispatches, total_shots, level):
    return filter_dispatches_by_policy(dispatches, total_shots, {
        "total_cost": -1,
        "total_time": 0,
        "used_computers": 0,
        "shots_difference": 0
    }, level)

def time_aware(dispatches, total_shots, level):
    return filter_dispatches_by_policy(dispatches, total_shots, {
        "total_cost": 0,
        "total_time": -1,
        "used_computers": 0,
        "shots_difference": 0
    }, level)

def get_dispatch_reliability(dispatch, total_shots):
    used_computers = get_dispatch_len(dispatch)
    shots_difference = get_dispatch_deviation(dispatch, total_shots)
    reliability = used_computers * (1 - shots_difference / total_shots)
    print(dispatch, reliability)
    return reliability

def reliable(dispatches, total_shots, level):
    percentage = 100 - level
    new_size = math.ceil((len(dispatches) * percentage) / 100)
    dispatches.sort(key = lambda dispatch: get_dispatch_reliability(dispatch, total_shots), reverse = True)
    return dispatches[:new_size]
    