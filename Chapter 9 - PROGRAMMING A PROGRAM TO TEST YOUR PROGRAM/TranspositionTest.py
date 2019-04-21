#! python3
# Chapter 9 Project - Program to test TranspositionEncrypt and TranspositionDecrypt

import random, sys, TranspositionDecrypt, TranspositionEncrypt

def main():
    random.seed(42) # Intialize the seed to a static # for now

    for i in range(20): # Run 20 test cases
        # Generate random messages to test

        # The message will have a random length
        message =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Convert the message string to a list to shuffle it
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)  # Convert the list back to a string

        print("Test #%s: %s..." % (i, message[:50]))

        # Check all possible keys for each message:
        for key in range(1, int(len(message) / 2)):
            encrypted = TranspositionEncrypt.encryptMessage(key, message)
            decrypted = TranspositionDecrypt.decryptMessage(key, encrypted)

            # If the decryption doesn't match the plaintext message, print an error and quit:
            if message != decrypted:
                print("Mismatch with key %s and message %s." % (key, message))
                print("Decrypted as %s: " % decrypted)
                sys.exit()

    print("Transposition cipher test passed.")

# If TranspositionTest.py is run (instead of imported as a module) call the main() function:
if __name__ == '__main__':
        main()