# Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def gameOfThrones(s):
    # Count the frequency of each character in the string
    char_count = Counter(s)
    
    # Count how many characters have an odd frequency
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
            
    # A palindrome can have at most one character with an odd frequency
    if odd_count <= 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()