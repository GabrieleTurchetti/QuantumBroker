from policy_handler import filter_dispatches_by_policy

def policy_is_valid(policy):
    try:
        if policy["weights"]["cost"] < -1 or policy["weights"]["cost"] > 1:
            return False

        if policy["weights"]["eco_sustainability"] < -1 or policy["weights"]["eco_sustainability"] > 1:
            return False

        if policy["weights"]["time"] < -1 or policy["weights"]["time"] > 1:
            return False

        if policy["weights"]["reliability"] < -1 or policy["weights"]["reliability"] > 1:
            return False

        if policy["weights"]["uniformity"] < -1 or policy["weights"]["uniformity"] > 1:
            return False

        if policy["level"] < 1 or policy["level"] > 99:
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
            "cost": 1,
            "eco_sustainability": 1,
            "time": 1,
            "reliability": 1,
            "uniformity": 1
        }, 99)

    dispatch = new_dispatches[0]
    return dispatch