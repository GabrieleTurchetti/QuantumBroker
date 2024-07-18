# Equal policy
def get_distribution_by_equal_policy(results):
    total_distribution = {}
    results_shots = {}
    total_shots = 0

    # For each computer in the results
    for result in results:
        result = result.to_dict()
        total_shots += result["shots"]

        # For a computer results, add the values in a dictionary
        for key, value in result["data"].items():
            if key in results_shots:
                results_shots[key] += value
            else:
                results_shots[key] = value

    # Calculate the final distribution
    for key, value in results_shots.items():
        total_distribution[key] = f"{round(value * 100 / total_shots, 2)}%"

    return total_distribution

# Fair policy
def get_distribution_by_fair_policy(results):
    total_distribution = {}
    partial_distributions_sum = {}

    # For each computer in the results
    for result in results:
        partial_distribution = result.distribution() # Get the partial distribution of a computer results

        # For each entry of the partial distribution, add the value in a dictionary
        for key, value in partial_distribution.items():
            if key in partial_distributions_sum:
                partial_distributions_sum[key] += value
            else:
                partial_distributions_sum[key] = value

    # Calculate the final distribution
    for key, value in partial_distributions_sum.items():
        total_distribution[key] = f"{round(value * 100 / len(results), 2)}%"

    return total_distribution