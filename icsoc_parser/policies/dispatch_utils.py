def get_dispatch_len(dispatch):
    length = 0

    for _, _, shots in dispatch["dispatch"]:
        if shots != 0:
            length += 1

    return length

def get_dispatch_deviation(dispatch, total_shots):
    avg = total_shots / get_dispatch_len(dispatch)
    sum = 0

    for _, _, shots in dispatch["dispatch"]:
        if shots != 0:
            sum += abs(shots - avg)

    deviation = sum / get_dispatch_len(dispatch)
    return deviation