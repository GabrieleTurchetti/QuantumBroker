from policies import lowcost, fast, accurate, fair, balanced

def policy_is_valid(policy):
    name = policy.split("-")[0]
    level = int(policy.split("-")[1])

    if (name != "lowcost" and name != "fast" and name != "accurate" and name != "fair" and name != "balanced"):
        return False

    if (level < 1 or level > 99):
        return False

    return True

def filter_dispatches_by_policies(dispatches, total_shots, policies):
    new_dispatches = dispatches

    for policy in policies:
        if (not policy_is_valid(policy)):
            raise Exception("Policy not valid")

        policy_name = policy.split("-")[0]
        policy_level = int(policy.split("-")[1])
        policy_func = eval(policy_name)
        new_dispatches = policy_func(new_dispatches, total_shots, policy_level)

    if len(new_dispatches) > 1:
        new_dispatches = balanced(new_dispatches, total_shots, 99)

    dispatch = new_dispatches[0]
    return dispatch