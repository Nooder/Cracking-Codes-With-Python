#! python3
# Chapter 8 Project - Transposition Cipher Decryption

import math

# Setup
key = 8
ciphertext = 'Cenoonommstmme oo snnio. s s c'
# Number of columns in transposition grid
numColumns = int(math.ceil(len(ciphertext) / float(key)))
# Number of rows in the transposition grid
numRows = key
# Number of "empty cells" left in the grid
numEmptyCells = numColumns * numRows - len(ciphertext)

# Each string in plaintext represents a column in the grid
plaintext = [''] * numColumns

# Setup indices to track progress
column = 0
row = 0

# Decrypt the ciphertext
for symbol in ciphertext:
    plaintext[column] += symbol
    column += 1     # Point to next column

    # If there are no more columns OR we're at the emptyCell, go back
    # to the first column and the next row to process
    if (column == numColumns) or (column == numColumns - 1 and \
        row >= numRows - numEmptyCells):
        column = 0
        row += 1

print(''.join(plaintext))