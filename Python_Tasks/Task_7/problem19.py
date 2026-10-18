# Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Set to store all possible uniform weights
    weights = set()
    current_weight = 0
    prev_char = ''
    
    # Calculate weights of all contiguous uniform substrings
    for char in s:
        # Get the character weight (a=1, b=2, ..., z=26)
        char_weight = ord(char) - ord('a') + 1
        
        if char == prev_char:
            current_weight += char_weight
        else:
            current_weight = char_weight
            prev_char = char
            
        weights.add(current_weight)
        
    # Answer each query
    result = []
    for q in queries:
        if q in weights:
            result.append("Yes")
        else:
            result.append("No")
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result) + '\n')

    fptr.close()