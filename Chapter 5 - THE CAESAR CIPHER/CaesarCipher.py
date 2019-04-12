#! python3
# Chapter 5 Project - Caesar Cipher
# USAGE: CaesarCipher.py <text> <key> <mode>
#        text = plaintext or ciphertext, key = encryption key (eg. 22)
#        mode = "encrypt" or "decrypt"

import sys, logging

# Get user input for text and key
if len(sys.argv) < 4:
    print("USAGE: CaesarCipher.py <text> <key> <mode>")
    print("text = plaintext or ciphertext, key = encryption key (eg. 22),", end="")
    print("mode = 'encrypt' or 'decrypt'")
    sys.exit()

# Setup. SYMBOLS = All supported characters that will be encrypted/decrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'
key = int(sys.argv[-2])
symbols_length = len(SYMBOLS)
plaintext = " ".join(sys.argv[1:-2])
mode = sys.argv[-1]
resultText = ""
translatedIndex = 0

# Start process with the provided key
for symbol in plaintext:
    # Check for non-supported symbols (won't be encrypted)
    if symbol in SYMBOLS:
        translatedIndex = SYMBOLS.find(symbol)  
        # Check mode
        if mode == 'encrypt':
            translatedIndex += key
        elif mode == 'decrypt':
            translatedIndex -= key

        # Handle wraparound > and <
        if translatedIndex > symbols_length:
            translatedIndex -= symbols_length
        elif translatedIndex < 0:
            translatedIndex += symbols_length

        # Perform substitution
        resultText += SYMBOLS[translatedIndex]
    # Append non-supported symbols as-is
    else:
        resultText += symbol

print("Complete. Here's the result of %s:\n" % mode)
print(resultText)