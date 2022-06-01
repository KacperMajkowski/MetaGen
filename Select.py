from Greedy_algorythm import greedy_alogrythm
from Misc_functions import generateRandomPermutation, calculateDistance

def initial_select(distance_matrix, lenght, elite_percent): # lenght - amount of initial paths, elite_percent - Percentage of paths made by greedy algorythm
    initial_paths = []
    elites = round(lenght*elite_percent/100)
    for i in range(elites):
        permutation = greedy_alogrythm(distance_matrix, i%len(distance_matrix))
        permutation_length = calculateDistance(permutation, distance_matrix)
        initial_paths.append([permutation, permutation_length])
    for i in range(lenght - elites):
        permutation = generateRandomPermutation(len(distance_matrix))
        permutation_length = calculateDistance(permutation, distance_matrix)
        initial_paths.append([permutation, permutation_length])

    return initial_paths

def select(distance_matrix)
