#! python3
# Chapter 7 Project - Transposition Cipher Encryption

def main():
        plaintext = "Common sense is not so common."
        key = 8
        cipherText = encryptMessage(key, plaintext)
        print(cipherText)

def encryptMessage(key, message):
        # Each string in ciphertext represents a column in the grid
        cipherText = [''] * key

        # Loop through each column in ciphertext
        for column in range(key):
                currentIndex = column

                # Keep looping until currentIndex goes past the message length
                while currentIndex < len(message):
                        # Place the character at the currentIndex in message
                        # at the end of the current column in the ciphertext list
                        cipherText[column] += message[currentIndex]

                        # Move currentIndex over
                        currentIndex += key

        # Convert the ciphertext list in to a string to return it
        returnText = "".join(cipherText)
        return returnText

# If TranspositionEncypt.py is run (instead of imported as a module) call the main() function:
if __name__ == '__main__':
        main()