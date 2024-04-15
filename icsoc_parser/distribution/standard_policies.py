# equal policy
def get_distribution_by_equal_policy(results):
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

def get_partial_distribution(result):
    result = result.to_dict()
    partial_distribution = {}

    for key, value in result["data"].items():
        partial_distribution[key] = value * 100 / result["shots"]

    return partial_distribution

# fair policy
def get_distribution_by_fair_policy(results):
    total_distribution = {}
    partial_distributions_sum = {}

    for result in results:
        partial_distribution = get_partial_distribution(result)

        for key, value in partial_distribution.items():
            if key in partial_distributions_sum:
                partial_distributions_sum[key] += value
            else:
                partial_distributions_sum[key] = value

    for key, value in partial_distributions_sum.items():
        total_distribution[key] = f"{round(value / len(results), 2)}%"

    return total_distribution