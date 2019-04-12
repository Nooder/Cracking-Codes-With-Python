#! python3
# Chapter 6 Project - Caesar Cipher Brute Force Hacker

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Loop through every possible key
for key in range(len(SYMBOLS)):
    decryptedText = ""
    decryptedIndex = 0

    # Loop through each symbol in the message
    for symbol in message:
        if symbol in SYMBOLS:
            decryptedIndex = SYMBOLS.find(symbol)
            decryptedIndex -= key

            # Handle wraparound <
            if decryptedIndex < 0:
                decryptedIndex += len(SYMBOLS)

            # Append the decrypted symbol
            decryptedText += SYMBOLS[decryptedIndex]
        # Skip non-supported symbols
        else:
            decryptedText += symbol

    # Print the result "decrypted" text using this key
    print("Decrypting with key=%s gave us: %s" % (key, decryptedText))