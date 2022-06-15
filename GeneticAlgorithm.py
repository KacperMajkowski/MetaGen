from Select import initial_select
from Select import select
from Crossing import crossPopulation
from Mutating import mutatePopulation


def geneticAlgorithm(distance_matrix, amount_of_paths, elite_percent, loops, tournament_size, mutation_chance):
     
    # Starting population
    population = initial_select(distance_matrix, amount_of_paths, elite_percent)

    # For stop condition
    for loop in range(loops):
        
        # Select
        population = select(tournament_size, population)
    
        # Crossing
        population = crossPopulation(distance_matrix, population)
        
        # Mutation
        population = mutatePopulation(distance_matrix, population, mutation_chance)
        
    return population

