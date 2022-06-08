import random

from Greedy_algorythm import greedy_alogrythm
from Misc_functions import generateRandomPermutation, calculateDistance


def initial_select(distance_matrix, paths_amount,
                   elite_percent):  # lenght - amount of initial paths, elite_percent - Percentage of paths made by greedy algorythm
    initial_paths = []
    elites = round(paths_amount * elite_percent / 100)
    for i in range(elites):
        permutation = greedy_alogrythm(distance_matrix, i % len(distance_matrix))
        permutation_length = calculateDistance(permutation, distance_matrix)
        initial_paths.append([permutation, permutation_length])
    for i in range(paths_amount - elites):
        permutation = generateRandomPermutation(len(distance_matrix))
        permutation_length = calculateDistance(permutation, distance_matrix)
        initial_paths.append([permutation, permutation_length])

    return initial_paths

def find_turnament_winner(turnament):
    min = 100000000000
    for path in turnament:
        if(path[1] < min):
            min = path[1]
            final_path = path
    return final_path


def select(turnament_size, paths):
    turnament_winners = []
    for i in range(len(paths)):
        turnament = []
        for j in range(turnament_size):
            turnament.append(random.choice(paths))
        turnament_winners.append(find_turnament_winner(turnament))
    print(turnament_winners)
