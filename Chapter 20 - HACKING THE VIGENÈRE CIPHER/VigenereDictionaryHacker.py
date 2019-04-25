#!python3
# Chapter 20 Project - Hacking the Vigenere Cipher using a dictionary attack

import DetectEnglish, VigenereCipher

def main():
    ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
    hackedMessage = hackVigenereDictionary(ciphertext)

    if hackedMessage != None:
        print("Successfully hacked message:\n")
        print(hackedMessage)
    else:
        print("Failed to hack encryption.")

def hackVigenereDictionary(ciphertext):
    fo = open('dictionary.txt')
    lines = fo.readlines()
    fo.close()

    for word in lines:
        word = word.strip() # Remove the newline character at the end
        decryptedText = VigenereCipher.decryptMessage(word, ciphertext)
        if DetectEnglish.isEnglish(decryptedText, wordPercentage=40):
            # Check with user to see if the decrypted key has been found:
            print()
            print("Possible encryption break:")
            print("Key: " + str(word) + ': ' + decryptedText[:100])
            print()
            print("Enter 'D' for done or just press <Enter> to continue breaking:")
            response = input("> ")

            if response.upper().startswith('D'):
                return decryptedText

if __name__ == '__main__':
    main()