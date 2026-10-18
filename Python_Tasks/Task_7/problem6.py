# Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def pangrams(s):
    # Convert string to lowercase and find all unique alphabetic characters
    letters = set(c.lower() for c in s if c.isalpha())
    
    # If the set contains all 26 letters, it's a pangram
    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()