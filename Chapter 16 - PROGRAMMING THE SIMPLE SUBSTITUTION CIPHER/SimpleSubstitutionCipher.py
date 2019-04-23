#!python3
# Chapter 16 Project - The Simple Substition Cipher (26! possible keys if brute forced)

import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message = '''If a man is offered a fact which goes against his
          instincts, he will scrutinize it closely, and unless the evidence
          is overwhelming, he will refuse to believe it. If, on the other
          hand, he is offered something which affords a reason for acting
          in accordance to his instincts, he will accept it even on the
          slightest evidence. The origin of myths is explained in this way.
          -Bertrand Russell'''
    key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    mode = 'encrypt'    # Set to 'encrypt' or 'decrypt'

    if not keyIsValid(key):
        sys.exit("There is an error in the key or symbol set.")
    if mode == 'encrypt':
        translated = encryptMessage(key, message)
    elif mode == 'decrypt':
        translated = decryptMessage(key, message)
    
    print("Using key %s" % key)
    print("The %sed message is:" % mode)
    print(translated)

# Check to make sure the key has exactly one of each letter in the English alphabet
def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()

    return keyList == lettersList

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA
    
    # Loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/Decrypt the symbol:
            symbolIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symbolIndex].upper()
            else:
                translated += charsB[symbolIndex].lower()
        else:
            # Symbol is not in LETTERS, so just append it:
            translated += symbol
    
    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()