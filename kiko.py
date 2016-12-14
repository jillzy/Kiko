import random
from random import randint
import bisect
import collections

# the mood of the line
# plays a role in determining style
moods = ["disbelief", "anger", "irreverent"]

def cdf(weights):
    total = sum(weights)
    result = []
    cumsum = 0
    for w in weights:
        cumsum += w
        result.append(cumsum / total)
    return result

def choice(population, weights):
    assert len(population) == len(weights)
    cdf_vals = cdf(weights)
    x = random.random()
    idx = bisect.bisect(cdf_vals, x)
    return population[idx]

def returnWeights(mood):
    return {
        'disbelief': [0.0, 0.1, 0.9, 0.0],
        'anger': [0.0, 0.1, 0.1, 0.9],
        'irreverent': [0.9, 0.1, 0.1, 0.0]
    }[mood]

def main():
    mood = moods[randint(0,2)]
    weights = returnWeights(mood)
    population = 'ABCD'
    counts = collections.defaultdict(int)
    letter = choice(population, weights)
    style = {"A": "p", "B": "c", "C": "sp", "D": "sl"}
    print (style.get(letter))


main()