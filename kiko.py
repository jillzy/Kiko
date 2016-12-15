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



"""change the ifs into a dict of the word and its typo/ should the ur stuff be slang?
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


def randomTypo(): #this is bad when you do multiple operations on the same word, use order control

    def double(w):  # dont replace punctuation with typo, will deal with grammar using span, don't double the same letter (kkikko)
        print("double")
        chars = [] #!!! replace the original word string (not char array) with new_w to retain grammar
        new = ""
        tmp = ""
        for c in w:
            if c not in ["!", ",", '"', "'", "?", "-"]:
                tmp += c
                chars.append(c)
        idx = randint(0, len(chars) - 1)
        letter = chars[idx]
        letter += letter
        chars[idx] = letter
        for c in chars:
            new += c
        w = w.replace(tmp, new)
        return w

    def omit(w): #omitting twice :( (hey i'm ik (kiko))
        print("omit")
        if len(w) > 4:
            chars = []
            tmp = ""
            new = ""
            for c in w:
                if c not in ["!", ",", '"', "'", "?", "-"]:
                    tmp += c
                    chars.append(c)
            chars[randint(0, len(chars) - 1)] = ""
            for c in chars:
                new += c
            w = w.replace(tmp, new)
            return w
        return w

    def switch(w): #omitting twice :( (hey i'm ik (kiko))
        print("switch")
        if len(w) > 3:
            tmp_w = ""
            new_w = ""
            chars = []
            for c in w:
                if c not in ["!", ",", '"', "'", "?", "-"]:
                    tmp_w += c
                    chars.append(c)
            idx = randint(1, len(tmp_w)-2)
            if idx is len(tmp_w)-2: #2nd last char
                t = chars[idx-1]
                chars[idx-1] = chars[idx]
                chars[idx] = t
            else:
                t = chars[idx]
                chars[idx] = chars[idx+1]
                chars[idx+1] = t
            for c in chars:
                new_w += c
            w = w.replace(tmp_w, new_w) #you awnna tighf, do you awtn to fight
            print(chars)
            print("new: " + new_w)
            print("old: " + tmp_w)
            print("replacement: " + w)

            return w
        return w

    fns = {
        0: switch,
        1: switch,
        2: switch
    }
    i = randint(0, len(fns)-1)
    return fns[i]


def determineTypos(sentence):
    i = randint(0, 9)
    if 0 <= i <= 1:  # i want to weights to depend on sentence length, eventually
        typos = 0
    elif 2 <= i <= 4:
        typos = 1
    elif 5 <= i <= 8:
        typos = 2
    elif i == 9:
        typos = 3

    new = ""
    for i in range(0, typos): #can operate on same sentence twiece
        k = randint(0, len(sentence) - 1)
        fn = randomTypo()
        sentence[k] = fn(sentence[k])
    for word in sentence:
        new += (word + " ")
    return new


def convertTone(s, l):
    #if "spell" in s:
    sentence = l.split()
    l = determineTypos(sentence)
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