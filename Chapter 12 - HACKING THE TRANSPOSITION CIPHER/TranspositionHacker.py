#!python3
# Chapter 12 Project - Hacking the Transposition Cipher

import DetectEnglish, TranspositionDecrypt

def main():
    message = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh
    na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no
    euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain
    one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp
    ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh
    gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr
    aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    hackedMessage = hackTransposition(message)

    if hackedMessage == None:
        print("Failed to hack encryption.")
    else:
        print("Successfully hacked message:\n")
        print(hackedMessage)

def hackTransposition(message):
    print("Hacking...")
    print("(Press Ctrl-C (On Windows) or Ctrol-D (On Mac/Linux) to quit at any time.)")

    # Brute force by looping through every possible key
    for key in range(1, len(message)):
        print("Trying key #%s..." % key)

        decryptedText = TranspositionDecrypt.decryptMessage(key, message)

        if DetectEnglish.isEnglish(decryptedText):
            # Ask user if this is the correct decryption:
            print()
            print("Possible encyption hack.")
            print("Key %s: %s" % (key, decryptedText[:100]))
            print()
            print("Enter D if done, or anything else to continue hacking:")
            response = input("> ")

            # Success
            if response.strip().upper().startswith("D"):
                return decryptedText
    
    # Brute force decryption failed
    return None

if __name__ == '__main__':
    main()