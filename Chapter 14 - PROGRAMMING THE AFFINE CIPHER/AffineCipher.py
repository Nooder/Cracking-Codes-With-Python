#!python3
# Chapter 14 Project - Affine Cipher

import sys, CryptoMath, random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def main():
    message = """"A computer would deserve to be called intelligent\
          if it could deceive a human into believing that it was human."\
          -Alan Turing"""
    key = getRandomKey()
    mode = 'encrypt'    # Set to either 'encypt' or 'decrypt'

    if mode == 'encrypt':
        translatedMessage = encryptMessage(key, message)
    elif mode == 'decrypt':
        translatedMessage = decryptMessage(key, message)

    print("Key: %s" % key)
    print("%sed text:" % mode.title())
    print(translatedMessage)

# Split the single key in to the multiplicaton (A) key plus the addition key (B)
def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

# Check for validity of the keys
def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit("Cipher is weak if key A is 1. Choose a different key.")
    if keyB == 0 and mode == 'encrypt':
        sys.exit("Cipher is weak if key B is 0. Choose a different key.")
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit("Key A must be greater than 0 and Key B must be \
            between 0 and %s." % (len(SYMBOLS) - 1))
    if CryptoMath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit("Key A (%s) and the symbol set size (%s) are not \
            relatively prime. Choose a different key." % (keyA, len(SYMBOLS)))

def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    cipherText = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # Encrypt the symbol
            symbolIndex = SYMBOLS.find(symbol)
            cipherText += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            cipherText += symbol    # Append the symbol without encrypting it
    return cipherText

def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plainText = ''
    modInverseOfKeyA = CryptoMath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # Decrypt the symbol
            symbolIndex = SYMBOLS.find(symbol)
            plainText += SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plainText += symbol # Append the symbol without decrypting it
    return plainText

# Generate a random key and check if the GCD relative to the symbol set is 1
def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if CryptoMath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

# If AffineCipher.py is run (instead of imported as a module), call
# the main() function
if __name__ == '__main__':
    main()