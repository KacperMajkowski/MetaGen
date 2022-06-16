from Select import initial_select
from Select import select
from Crossing import crossPopulation
from Mutating import mutatePopulation
from Misc_functions import getBestSpecimen


def geneticAlgorithm(distance_matrix, amount_of_paths, elite_percent, loops,  # Initial
                     select_type, tournament_size, max_age,                   # Select
                     crossing_chance, crossing_function,                      # Crossing
                     mutation_chance):                                        # Mutation
     
    # Starting population
    population = initial_select(distance_matrix, amount_of_paths, elite_percent)

    # For stop condition
    for loop in range(loops):
        
        # Select
        population = select(tournament_size, population, select_type, max_age)
    
        # Crossing
        population = crossPopulation(distance_matrix, population, crossing_chance, crossing_function)
        
        # Mutation
        population = mutatePopulation(distance_matrix, population, mutation_chance)

    best = getBestSpecimen(population)
    print('Best permutation:', best[0])
    print('Best length:', best[1])
    return population

