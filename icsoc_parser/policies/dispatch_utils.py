def get_dispatch_len(dispatch):
    length = 0

    for _, _, shots in dispatch["dispatch"]:
        if shots != 0:
            length += 1

    return length

def get_dispatch_deviation(dispatch, total_shots):
    used_computers = get_dispatch_len(dispatch)
    avg = total_shots / used_computers
    sum = 0

    for _, _, shots in dispatch["dispatch"]:
        if shots != 0:
            sum += abs(shots - avg)

    deviation = sum / used_computers
    return deviation