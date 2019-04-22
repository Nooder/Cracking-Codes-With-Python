#!python3
# Chapter 15 Project - Hacking the Affine Cipher

import AffineCipher, CryptoMath, DetectEnglish

SILENT_MODE = False

def main():
    message =  """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""
    
    hackedMessage = hackAffine(message)

    if hackedMessage != None:
        # Display the plaintext that was decrypted
        print(hackedMessage)
    else:
        print("Failed to hack encryption.")

def hackAffine(message):
    print("Hacking...")

    # Allow program to stop on Windows or Linux respectively
    print("(Press Ctrl-C (Windows) or Ctrl-D (Mac/Linux) to stop at any time.)")

    # Brute force by looping through every possible key
    for key in range(len(AffineCipher.SYMBOLS) ** 2):
        keyA = AffineCipher.getKeyParts(key)[0]
        if CryptoMath.gcd(keyA, len(AffineCipher.SYMBOLS)) != 1:
            continue
        
        decryptedText = AffineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print("Tried Key %s... (%s)" % (key, decryptedText))
        
        if DetectEnglish.isEnglish(decryptedText):
            # Check with the user if the decrypted text has been found
            print()
            print("Possible encryption hack:")
            print("Key: %s" % key)
            print("Decrypted message: %s" % decryptedText[:200])
            print()
            print("Enter 'D' for done, or just press Enter to continue hacking:")
            response = input("> ")

            # Success
            if response.upper().strip().startswith("D"):
                return decryptedText
    # Failed to find plaintext
    return None

# If AffineHacker.py was run (instead of imported as a module), call
# the main() function
if __name__ == '__main__':
    main()