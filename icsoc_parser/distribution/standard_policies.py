# equal policy
def get_distribution_by_equal_policy(results):
    total_distribution = {}
    results_shots = {}
    total_shots = 0

    for result in results:
        result = result.to_dict()
        total_shots += result["shots"]

        for key, value in result["data"].items():
            if key in results_shots:
                results_shots[key] += value
            else:
                results_shots[key] = value

    for key, value in results_shots.items():
        total_distribution[key] = f"{round(value * 100 / total_shots, 2)}%"

    return total_distribution

# fair policy
def get_distribution_by_fair_policy(results):
    total_distribution = {}
    partial_distributions_sum = {}

    for result in results:
        partial_distribution = result.distribution()

        for key, value in partial_distribution.items():
            if key in partial_distributions_sum:
                partial_distributions_sum[key] += value
            else:
                partial_distributions_sum[key] = value

    for key, value in partial_distributions_sum.items():
        total_distribution[key] = f"{round(value * 100 / len(results), 2)}%"

    return total_distribution