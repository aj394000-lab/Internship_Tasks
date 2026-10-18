# Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

def isValid(s):
    # Count the frequency of each character
    char_counts = Counter(s)
    
    # Count how often each frequency appears
    freq_counts = Counter(char_counts.values())
    
    # If all characters have the same frequency, it's valid
    if len(freq_counts) == 1:
        return "YES"
    
    # If there are more than 2 different frequencies, it cannot be made valid by removing 1 character
    if len(freq_counts) > 2:
        return "NO"
    
    # Get the two unique frequencies and their counts
    freqs = list(freq_counts.keys())
    counts = list(freq_counts.values())
    
    f1, f2 = freqs[0], freqs[1]
    c1, c2 = counts[0], counts[1]
    
    # Condition 1: One of the frequencies is 1 and it occurs only once (we can remove that single character)
    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        return "YES"
        
    # Condition 2: The difference between the two frequencies is 1, and the higher frequency occurs only once
    if (abs(f1 - f2) == 1) and ((f1 > f2 and c1 == 1) or (f2 > f1 and c2 == 1)):
        return "YES"
        
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()