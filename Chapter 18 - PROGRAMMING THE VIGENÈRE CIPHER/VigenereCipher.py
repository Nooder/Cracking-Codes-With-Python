#!python3
# Chapter 18 Project - The Vigenère Cipher

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    message =  """Alan Mathison Turing was a British mathematician,
          logician, cryptanalyst, and computer scientist."""
    key = 'ASIMOV'
    mode = 'encrypt'    # Set to either 'encypt' or 'decrypt'

    if mode == 'encrypt':
        translated = encryptMessage(key, message)
    elif mode == 'decrypt':
        translated = decryptMessage(key, message)

    print("%sed message:" % mode.title())
    print(translated)

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = [] # Stores the ecrypted/decrypted message string

    keyIndex = 0
    key = key.upper()

    for symbol in message:  # Loops through each symbol in the message
        num = LETTERS.find(symbol.upper())
        if num != -1:   # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])  # Add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])  # Subtract if decrypting

            num %= len(LETTERS)    # Handle any wraparound

            # Add the encrypted/decrypted symbol to the end of translated
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1   # Move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # Append the symbol without encrypting/decrypting
            translated.append(symbol)
    
    return ''.join(translated)

if __name__ == '__main__':
    main()