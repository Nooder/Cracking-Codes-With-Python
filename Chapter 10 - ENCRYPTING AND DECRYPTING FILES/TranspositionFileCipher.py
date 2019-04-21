#! python3
# Chapter 10 Project - Use Transposition Ecryption and Decryption on files

import time, os, sys, TranspositionDecrypt, TranspositionEncrypt

def main():
    #inputFilename = 'frankenstein.txt'
    inputFilename = 'frankenstein_encrypted.txt'
    outputFilename = 'frankenstein_decrypted.txt'
    key = 10
    mode = 'decrypt'    # Set to 'encrypt' or 'decrypt'

    # If the input file does not exist, the program terminates early
    if not os.path.exists(inputFilename):
        print("The file %s does not exist. Quitting..." % inputFilename)
        sys.exit()
    
    # If the output file already exists, give the user a chance to exit
    # (Otherwise the file will be overwritten)
    if os.path.exists(outputFilename):
        print("This will overwrite the file %s. (C)ontinue or (Q)uit?" % outputFilename)
        response = input(">")
        if response.lower().startswith("Q"):
            sys.exit()
        
    # Read the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print("%sing..." % mode.title())

    # Measure how long the encryption/decryption takes
    startTime = time.time()
    if mode == 'encrypt':
        translated = TranspositionEncrypt.encryptMessage(key, content)
    elif mode == 'decrypt':
        translated = TranspositionDecrypt.decryptMessage(key, content)
    totalTime = round(time.time() - startTime, 2)
    print("%sion time: %s seconds" % (mode.title(), totalTime))

    # Write out the translated message to the output file
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print("Done %sing %s (%s characters)." % (mode, inputFilename, len(content)))
    print("%sed file is %s." % (mode.title(), outputFilename))

# If TranspositionFileCipher.py is run (instead of imported as a module)
# call the main() function:
if __name__ == '__main__':
    main()