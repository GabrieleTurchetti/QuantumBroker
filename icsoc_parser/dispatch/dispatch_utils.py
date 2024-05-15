import math

# Get the shots difference of a dispatch
def get_dispatch_mean_deviation(dispatch, total_shots):
    used_computers = len(dispatch["dispatch"])
    avg = total_shots / used_computers
    sum = 0

    for _, _, shots in dispatch["dispatch"]:
        if shots != 0:
            sum += abs(shots - avg)

    deviation = sum / used_computers
    return deviation

def get_metric_mean(values):
    avg = sum(values) / len(values)
    return avg

def get_metric_standard_deviation(values):
    tot = 0
    avg = sum(values) / len(values)

    for value in values:
        tot += (value - avg) ** 2

    deviation = math.sqrt(tot / len(values))
    return deviation