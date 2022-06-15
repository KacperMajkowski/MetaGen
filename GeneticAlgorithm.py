from Select import initial_select
from Select import select
from Crossing import crossPopulation
from Mutating import mutatePopulation


def geneticAlgorithm(distance_matrix, amount_of_paths, elite_percent,
                     loops, select_type, tournament_size, crossing_chance, mutation_chance):
     
    # Starting population
    population = initial_select(distance_matrix, amount_of_paths, elite_percent)

    # For stop condition
    for loop in range(loops):
        
        # Select
        population = select(tournament_size, population, select_type)
    
        # Crossing
        population = crossPopulation(distance_matrix, population, crossing_chance)
        
        # Mutation
        population = mutatePopulation(distance_matrix, population, mutation_chance)
        
    return population

