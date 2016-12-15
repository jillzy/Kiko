from __future__ import division  # Python 2 users only
import random
from random import randint
import bisect
import re


# the mood of the line
# plays a role in determining style
moods = ["disbelief", "anger", "irreverent"]
styles = {"A": "punct", "B": "caps", "C": "spell", "D": "slang", "E": "low"} #punc into span

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
    return { #punctuation, caps, bad spelling, slang, low
        # can this work with condition instead of string? e.g. mood < 3
        'disbelief': [0.1, 0.25, 0.25, 0.3, 0.1],
        'anger': [0.1, 0.45, 0.3, 0.1, 0.05],
        'irreverent': [0.1, 0.1, 0.25, 0.3, 0.25],
    }[mood]

def findStyle(mood):
    style = []
    population = 'ABCDE'
    for i in range(2):
        weights = returnWeights(mood)
        letter = choice(population, weights)
        style.append(styles.get(letter))
    style = set(style)
    return style

"""
def convertTone(mood): #instead of using this structure to convert mood, use to determine spans
    def aConvert(m, s, line):
        if "caps" in s:
            return line.upper()
    def iConvert(m, s, line):
        print("irrev")
    def dConvert(m, s, line):
        print("disb")

    return {
        'anger': aConvert,
        'irreverent': iConvert,
        'disbelief': dConvert

    }[mood]

"""

"""change the ifs into a dict of the word and its typo
insensitive = l.lower()
if "fuck" in insensitive:
    l = l.replace("fuck", "fcuk")
if "you're" in insensitive:
    l = l.replace("you're", "ur")
if "your" in insensitive:
    l = l.replace("youre", "ur")
if "your" in insensitive:
    l = l.replace("your", "ur")
if "you" in insensitive:
    l = l.replace("you", "u")"""


def double(w): #dont replace punctuation with typo, will deal with grammar using span
    tmp_w = ""
    for c in w:
        if c not in ["!", ",", '"', "'", "?", "-"]:
            tmp_w += c
    new_w = tmp_w
    original = new_w[randint(0, len(new_w)-1)]
    change = original + original
    new_w = new_w.replace(original, change)
    w = w.replace(tmp_w, new_w)

    return w

def makeTypo(sentence, typos):
    new = ""
    for i in range(0, typos): #can operate on same sentence twiece
        k = randint(0, len(sentence) - 1)
        sentence[k] = double(sentence[k]) #make many, omit, double, switch etc
    for word in sentence:
        new += (word + " ")
    return new

def determineNumberTypos():
    i = randint(0, 9)
    if 0 <= i <= 1:  # i want to weights to depend on sentence length, eventually
        typos = 0
    elif 2 <= i <= 4:
        typos = 1
    elif 5 <= i <= 8:
        typos = 2
    elif i == 9:
        typos = 3
    return typos

def convertTone(s, l):
    new = ""
    #if "spell" in s:
    sentence = l.split()
    typos = determineNumberTypos()
    l = makeTypo(sentence, typos)
    if "caps" in s:
        l = l.upper()
    elif "low" in s:
        l = l.lower()

    return l


def main():
    line = raw_input("hi im kiko i'll say a thing for u...: \n")
    mood = moods[randint(0, 2)]
    #print(mood)
    style = findStyle(mood)
    #print(style)
    #convert = convertTone(mood)
    #c1 = convert(mood, style, line)
    c1 = convertTone(style, line)
    print("\nkiko says: \n"+c1)



main()