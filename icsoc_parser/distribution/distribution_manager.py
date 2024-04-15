from .standard_policies import get_distribution_by_equal_policy, get_distribution_by_fair_policy

STANDARD_POLICIES = ["equal", "fair"]

def policy_is_valid(policy):
    if not policy in STANDARD_POLICIES:
        False
    
    return True

def get_distribution(results, policy):
    if not policy_is_valid(policy):
        raise Exception("Distribution policy not valid")

    distribution = {}

    match policy:
        case "equal":
            distribution = get_distribution_by_equal_policy(results)
        case "fair":
            distribution = get_distribution_by_fair_policy(results)

    return distribution
