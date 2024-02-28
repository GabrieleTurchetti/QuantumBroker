import math

# Lowcost policy
def lowcost(dispatches, total_shots, level):
    percentage = 100 - level
    new_size = math.ceil((len(dispatches) * percentage) / 100)
    dispatches.sort(key = lambda dispatch: list(dispatch["total_cost"])[0][0])
    return dispatches[:new_size]

# Fast policy
def fast(dispatches, total_shots, level):
    percentage = 100 - level
    new_size = math.ceil((len(dispatches) * percentage) / 100)
    dispatches.sort(key = lambda dispatch: list(dispatch["total_time"])[0][0])
    return dispatches[:new_size]

# Accurate policy
def accurate(dispatches, total_shots, level):
    percentage = 100 - level
    new_size = math.ceil((len(dispatches)* percentage) / 100)
    dispatches.sort(key = lambda dispatch: len(dispatch["dispatch"]), reverse = True)
    return dispatches[:new_size]

# Fair policy
def get_deviation(dispatch, total_shots):
    avg = total_shots / len(dispatch["dispatch"])
    dev = 0

    for _, _, shots in dispatch["dispatch"]:
        dev += abs(shots - avg)

    return dev

def fair(dispatches, total_shots, level):
    percentage = 100 - level
    new_size = math.ceil((len(dispatches) * percentage) / 100)
    dispatches.sort(key = lambda dispatch: get_deviation(dispatch, total_shots))
    return dispatches[:new_size]

# Balanced policy
def get_balancing(dispatch, total_shots):
    total_cost = list(dispatch["total_cost"])[0][0]
    total_time = list(dispatch["total_time"])[0][0]
    used_backends = len(dispatch["dispatch"])
    deviation = get_deviation(dispatch, total_shots)
    balancing = - total_cost * 10 - total_time + used_backends * 100 - deviation
    return balancing

def balanced(dispatches, total_shots, level):
    percentage = 100 - level
    new_size = math.ceil((len(dispatches) * percentage) / 100)
    dispatches.sort(key = lambda dispatch: get_balancing(dispatch, total_shots), reverse = True)
    return dispatches[:new_size]