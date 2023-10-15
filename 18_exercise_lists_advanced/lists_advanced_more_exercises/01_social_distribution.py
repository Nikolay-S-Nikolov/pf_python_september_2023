def is_wealth_distributed(population: list, min_wealth: int) -> bool:
    is__distributed = True
    for money in population:
        if money < min_wealth:
            is__distributed = False
    return is__distributed


def distribute_the_wealth(population: list, min_wealth: int):
    if sum(population) / len(population) < min_wealth:
        return f"No equal distribution possible"
    else:
        while not is_wealth_distributed(population, min_wealth):
            idx_max_number = population.index(max(population))
            idx_min_number = population.index(min(population))
            difference = min_wealth - population[idx_min_number]
            if population[idx_max_number] - difference < min_wealth:
                difference = population[idx_max_number] - min_wealth
            population[idx_max_number] -= difference
            population[idx_min_number] += difference
        return population


population_list = [int(num) for num in input().split(', ')]
minimum_wealth = int(input())

result = distribute_the_wealth(population_list, minimum_wealth)
print(result)
