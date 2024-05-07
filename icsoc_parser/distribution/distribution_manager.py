from .standard_policies import get_distribution_by_equal_policy, get_distribution_by_fair_policy

STANDARD_POLICIES = ["equal", "fair"] # List of standard dispatch policy names

# Check if a distribution policy is correctly formed
def policy_is_valid(policy):
    if not policy in STANDARD_POLICIES:
        False
    
    return True

# Main function that return the final distribution
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
