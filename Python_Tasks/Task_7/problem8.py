# Gemstones
# https://www.hackerrank.com/challenges/gem-stones/problem

import sys

def gemstones(arr):
    common = set(arr[0])
    for s in arr[1:]:
        common &= set(s)
    return len(common)

if __name__ == '__main__':
    # Reads all inputs from standard input
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        arr = input_data[1:n+1]
        result = gemstones(arr)
        print(result)