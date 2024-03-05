from policy_handler import filter_dispatches_by_policy

def policy_is_valid(policy):
    try:
        if policy["level"] < 1 or policy["level"] > 99:
            return False

        for key, value in policy["weights"].items():
            if value < -1 or value > 1:
                return False

    except:
        return False

    return True

def filter_dispatches_by_policies(dispatches, total_shots, policies):
    if len(dispatches) < 1:
        raise Exception("No dispach found")

    new_dispatches = dispatches

    for policy in policies:
        if not policy_is_valid(policy):
            raise Exception("Policy not valid")

        if len(new_dispatches) == 1:
            break
            
        new_dispatches = filter_dispatches_by_policy(new_dispatches, total_shots, policy["weights"], policy["level"])

    if len(new_dispatches) > 1:
        new_dispatches = filter_dispatches_by_policy(new_dispatches, total_shots, {
            "total_cost": -1,
            "total_time": -1,
            "used_computers": 1,
            "shots_difference": -1
        }, 99)

    dispatch = new_dispatches[0]
    return dispatch