# Anagram
# https://www.hackerrank.com/challenges/anagram/problem

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the 'anagram' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.

def anagram(s):
    # If the length of the string is odd, we cannot split it into two equal parts
    if len(s) % 2 != 0:
        return -1
    
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    # Count character frequencies for both halves
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Calculate the number of changes required
    # Subtracting count2 from count1 leaves the excess characters in s1
    # that need to be replaced.
    diff = count1 - count2
    
    # Sum up the remaining counts to get the total changes needed
    return sum(diff.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()