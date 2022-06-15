import random


def swapRandom(permutation):
    i = random.randint(0, len(permutation) - 1)
    j = random.randint(0, len(permutation) - 1)
    while i == j:
        j = random.randint(0, len(permutation) - 1)
        
    permutation[i], permutation[j] = permutation[j], permutation[i]


def mutate(permutation, probability):
    if probability >= 100:
        return
    roll = random.randint(0, 100)
    while roll < probability:
        swapRandom(permutation)
        roll = random.randint(0, 100)

