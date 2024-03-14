from custom_policy import filter_dispatches_by_custom_policy
from standard_policies import filter_dispatches_by_cost_aware_policy, filter_dispatches_by_time_aware_policy, filter_dispatches_by_reliable_policy

STANDARD_POLICY = ["cost-aware", "time-aware", "reliable"]

def policy_is_valid(policy):
    if isinstance(policy, str):
        policy_name = "-".join(policy.split("-")[:-1])
        policy_level = int(policy.split("-")[-1])

        if not policy_name in STANDARD_POLICY:
            return False

        if policy_level < 1 or policy_level > 99:
            return False
    else:
        try:
            if policy["level"] < 1 or policy["level"] > 99:
                return False

            for key, value in policy["metrics"].items():
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
        
        if isinstance(policy, str):
            policy_name = "-".join(policy.split("-")[:-1])
            policy_level = int(policy.split("-")[-1])

            match policy_name:
                case "cost-aware":
                    new_dispatches = filter_dispatches_by_cost_aware_policy(new_dispatches, total_shots, policy_level)
                case "time-aware":
                    new_dispatches = filter_dispatches_by_time_aware_policy(new_dispatches, total_shots, policy_level)
                case "reliable":
                    new_dispatches = filter_dispatches_by_reliable_policy(new_dispatches, total_shots, policy_level)
        else:
            new_dispatches = filter_dispatches_by_custom_policy(new_dispatches, total_shots, policy["metrics"], policy["level"])

    if len(new_dispatches) > 1:
        new_dispatches = filter_dispatches_by_custom_policy(new_dispatches, total_shots, {
            "total_cost": -1,
            "total_time": -1,
            "used_computers": 1,
            "shots_difference": -1
        }, 99)

    dispatch = new_dispatches[0]
    return dispatch