from .custom_policy import filter_dispatches_by_custom_policy
from .standard_policies import filter_dispatches_by_cost_aware_policy, filter_dispatches_by_time_aware_policy, filter_dispatches_by_reliable_policy, filter_dispatches_by_green_policy

STANDARD_POLICIES = ["cost-aware", "time-aware", "reliable", "green"] # List of the standard distribution policy names

# Check if a distribution policy is correctly formed
def policy_is_valid(policy):
    if isinstance(policy, str):
        policy_name = "-".join(policy.split("-")[:-1])
        policy_level = int(policy.split("-")[-1])

        if not policy_name in STANDARD_POLICIES:
            return False

        if not isinstance(policy_level, int) or policy_level < 1 or policy_level > 99:
            return False
    else:
        try:
            if policy["level"] < 1 or policy["level"] > 99:
                return False

            for value in policy["metric_weights"].values():
                if not isinstance(value, int):
                    return False
        except:
            return False

    return True

# Main function that handle the list of the distribution policies in the request
def filter_dispatches_by_policies(dispatches, total_shots, policies):
    if len(dispatches) < 1:
        raise Exception("No dispach found")

    new_dispatches = dispatches

    for policy in policies:
        if not policy_is_valid(policy):
            raise Exception("Dispatch policy not valid")

        if len(new_dispatches) == 1:
            break
        
        # If is a standard distribution policy
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
                case "green":
                    new_dispatches = filter_dispatches_by_green_policy(new_dispatches, total_shots, policy_level)
        # If is a custom distribution policy
        else:
            new_dispatches = filter_dispatches_by_custom_policy(new_dispatches, total_shots, policy["metric_weights"], policy["level"])

    # If there are more than one dispatch, the last are filtered further with one general distribution policy
    if len(new_dispatches) > 1:
        new_dispatches = filter_dispatches_by_custom_policy(new_dispatches, total_shots, {
            "total_cost": -1,
            "total_energy_cost": -1,
            "total_time": -1,
            "used_computers": 1,
            "shots_difference": -1
        }, 1)

    dispatch = new_dispatches[0]
    return dispatch