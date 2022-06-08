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


def find_tournament_winner(turnament):
    min = 100000000000
    for path in turnament:
        if(path[1] < min):
            min = path[1]
            final_path = path
    return final_path


def select(tournament_size, paths):
    tournament_winners = []
    for i in range(len(paths)):
        tournament = []
        for j in range(tournament_size):
            tournament.append(random.choice(paths))
        tournament_winners.append(find_tournament_winner(tournament))
    print(tournament_winners)
