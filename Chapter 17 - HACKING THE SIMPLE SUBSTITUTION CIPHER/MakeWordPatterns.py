#!python3
# Chapter 17 Project - Module to create WordPatters.py to be used
# to hack the SimpleSubstitutionCipher

import pprint

# Create a dictionary of the pattern of the word of the form
# HELLO = 0.1.2.2.3         TEST = 0.1.2.0
def makeWordPattern(word):
    word = word.upper()
    index = 0
    charsSeen = {}
    result = []

    for char in word:
        if char not in charsSeen:
            charsSeen[char] = str(index)
            index += 1
        result.append(charsSeen[char])
    return '.'.join(result)

def main():
    allPatterns = {}

    fo = open("dictionary.txt")
    words = fo.read().split('\n')
    fo.close()

    # Create and assign the patterns to word(s) in allPatterns
    for word in words:
        pattern = makeWordPattern(word)

        if pattern in allPatterns:
            allPatterns[pattern].append(word)
        else:
            allPatterns[pattern] = [word]

    # Generate WordPatterns.py with allPatterns in it as a dict:
    fo = open('WordPatterns.py', 'w')
    fo.write('allPatterns = ')
    fo.write(pprint.pformat(allPatterns))
    fo.close()

if __name__ == '__main__':
    main()