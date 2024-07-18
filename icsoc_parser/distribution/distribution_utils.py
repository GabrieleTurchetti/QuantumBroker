import math

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