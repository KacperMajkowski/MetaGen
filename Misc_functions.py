import random


def generateRandomPermutation(length):
    permutation = []
    for i in range(length):
        permutation.append(i)

    random.shuffle(permutation)
    return permutation


def calculateDistance(permutation, distance_matrix):
    total_distance = 0
    for i in range(len(permutation)):
        total_distance += distance_matrix[permutation[i]][permutation[(i + 1) % len(permutation)]]
    return total_distance
        
