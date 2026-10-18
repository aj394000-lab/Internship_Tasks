# Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def separateNumbers(s):
    n = len(s)
    # The first number can be at most half the length of the string
    for i in range(1, n // 2 + 1):
        first_str = s[:i]
        # Skip if the first number has a leading zero
        if first_str.startswith('0'):
            break
            
        current = int(first_str)
        built_string = first_str
        
        # Build the sequence until its length is >= the original string's length
        while len(built_string) < n:
            current += 1
            built_string += str(current)
            
        # If the built string matches the original string, it's beautiful!
        if built_string == s:
            print(f"YES {first_str}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input().strip()
        separateNumbers(s)