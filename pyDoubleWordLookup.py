#!/usr/bin/env python3

import sys
import argparse
import re


def checkRegexPattern(regex, pattern):
    # print(regex.match(pattern))

    if not regex.match(pattern):
        print(f'Pattern {pattern} can only contain lowercase alphabetic characters or ? for unknown.')
        return 'bad'

    return 'good'


def checkPatterns(pattern1, pattern2):
    if len(pattern1) != len(pattern2):
        print('The two patterns must be the same length')
        return 'bad'

    ret = 'good'

    p = re.compile('^[a-z\?]*$')
    if checkRegexPattern(regex=p, pattern=pattern1) == 'bad':
        ret = 'bad'

    if checkRegexPattern(regex=p, pattern=pattern2) == 'bad':
        ret = 'bad'

    return ret


def buildWordMap():
    file = open('words_alpha.txt', "r")
    wordMap = {}
    for line in file:
        word = line.strip('\n')
        l = len(word)
        words = wordMap.get(l)
        newSet = {word}
        if not words:
            wordMap[l] = newSet
        else:
            words.update(newSet)
                    
    return wordMap


def printWordMap(wordMap):
    for l in wordMap:
        print(f'size: {l} \t num Words: {len(wordMap.get(l))}')


def findCommonPattern(pattern1, pattern2):
    cp = ""
    cc = 0
    for i in range(len(pattern1)):
        if pattern1[i] == pattern2[i] and pattern1[i] != '?':
            cp += pattern1[i]
            cc += 1
        else:
            cp += "[a-z]"

    if cc == 0:
        return ""

    return cp


def buildBestSearchSet(lwd, pattern1, pattern2):
    bigWordSet = lwd.get(len(pattern1))
    narrowPattern = findCommonPattern(pattern1=pattern1, pattern2=pattern2).replace("?", "[a-z]")
    # print(f'Narrow Pattern = {narrowPattern}')

    if narrowPattern:
        #print(len(bigWordSet))

        narrowSet = set()
        fCount = 0

        for word in bigWordSet:
            if word.startswith('f'):
                fCount += 1

            match = re.search(narrowPattern, word)

            if match:
                narrowSet.update({word})

        return narrowSet

    return bigWordSet


def buildPatternSet(searchSet, pattern):
    pSet = set()
    for x in searchSet:
        match = re.search(pattern, x)
        if match:
            pSet.add(x)
    return pSet


def createSubstitutionMap(pattern1, pattern2):
    subMap = dict()
    for i in range(len(pattern1)):
        if pattern1[i] != pattern2[i] and pattern2[i] != '?':
           subMap[i] = pattern2[i]

    return subMap


def replaceLetter(word, index, value):
    newWord=""
    lastIndex = len(word) - 1
    if index == 0:
        newWord = value + word[1:]
    elif index == lastIndex:
        newWord = word[0:lastIndex] + value
    else:
        newWord = word[0:index] + value + word[index+1:]

    return newWord

def findWordCombos(firstSet, secondSet, subMap):
    comboSet = set()
    for mainWord in firstSet:
        secondWord=mainWord

        for key in subMap.keys():
            secondWord = replaceLetter(word=secondWord, index=key, value=subMap.get(key))

        if secondWord in secondSet:
            combo = mainWord + " / " + secondWord
            comboSet.update({combo})

    return comboSet

def main():
    parser = argparse.ArgumentParser(
        description='Find words in dictionary against two patterns whose unknown letters match.')
    parser.add_argument('-p1', action='store', dest='pattern1',
                        help='First pattern to look up.')
    parser.add_argument('-p2', action='store', dest='pattern2',
                        help='Second pattern to look up.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0.1')

    args = parser.parse_args(sys.argv[1:])
    print(f'pattern1 = {args.pattern1}')
    print(f'pattern2 = {args.pattern2}')

    if checkPatterns(pattern1=args.pattern1, pattern2=args.pattern2) == 'good':
        chSubMap1 = createSubstitutionMap(pattern1=args.pattern1, pattern2=args.pattern2)
        pattern1 = args.pattern1.replace("?", "[a-z]")
        pattern2 = args.pattern2.replace("?", "[a-z]")
        lengthWordDictionary = buildWordMap()
        # printWordMap(wordMap=lengthWordDictionary)
        searchSet = buildBestSearchSet(lwd=lengthWordDictionary, pattern1=args.pattern1, pattern2=args.pattern2)
        # print(f'search set size: {len(searchSet)}')
        p1Set = buildPatternSet(searchSet=searchSet, pattern=pattern1)
        p2Set = buildPatternSet(searchSet=searchSet, pattern=pattern2)
        # print(f'p1Set size = {len(p1Set)} \t p2Set size = {len(p2Set)}')
        # print(p1Set)
        # print(p2Set)
        # print(chSubMap1)
        wordSet = sorted(findWordCombos(firstSet=p1Set, secondSet=p2Set, subMap=chSubMap1))
        for combo in wordSet:
            print(combo)



if __name__ == '__main__':
    main()