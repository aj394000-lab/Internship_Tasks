# Beautiful Binary String
# https://www.hackerrank.com/challenges/beautiful-binary-string/problem

import math
import os
import random
import re
import sys

def beautifulBinaryString(b):
    # Convert string to a list so we can modify characters if needed, 
    # or we can simply count while traversing.
    i = 0
    steps = 0
    b_list = list(b)
    
    while i <= len(b_list) - 3:
        if b_list[i] == '0' and b_list[i+1] == '1' and b_list[i+2] == '0':
            # Change the third character of the '010' substring to '1'
            b_list[i+2] = '1'
            steps += 1
            # Skip past this matched substring
            i += 3
        else:
            i += 1
            
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')
    fptr.close()