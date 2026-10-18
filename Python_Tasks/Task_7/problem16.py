# Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    encrypted = []
    # Ensure the shift wraps around the 26 letters of the alphabet
    k = k % 26
    
    for char in s:
        if 'a' <= char <= 'z':
            # Shift lowercase letters and wrap using modulo 26
            new_char = chr(ord('a') + (ord(char) - ord('a') + k) % 26)
            encrypted.append(new_char)
        elif 'A' <= char <= 'Z':
            # Shift uppercase letters and wrap using modulo 26
            new_char = chr(ord('A') + (ord(char) - ord('A') + k) % 26)
            encrypted.append(new_char)
        else:
            # Leave non-alphabetic characters (like hyphens or symbols) unchanged
            encrypted.append(char)
            
    return "".join(encrypted)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()