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


def makeTypo(w):
    tmp = ""
    new = ""
    for c in w:
        if c not in ["!", ",", '"', "'", "?", "-"]:
            tmp += c
    new = tmp[::-1]
    w = w.replace(tmp, new)
    return w

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
    if "spell" in s:
        #words = re.sub("[^\w]", " ", l).split() #split by " ", should count ' and ,  [^\w]
        words = l.split()
        typos = determineNumberTypos()
        for i in range(0, typos): #dont replace punctuation with typo, will deal with grammar using span
            k = randint(0,len(words)-1)
            words[k] = makeTypo(words[k])
            #words[k] = "typo"
        for word in words:
            new += (word + " ")
        l = new
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