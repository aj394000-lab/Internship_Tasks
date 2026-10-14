# No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Elements of the array
    arr = input_data[2:2 + n]
    
    # Sets A and B (stored as sets for O(1) lookups)
    A = set(input_data[2 + n : 2 + n + m])
    B = set(input_data[2 + n + m : 2 + n + 2 * m])
    
    # Calculate happiness
    happiness = 0
    for x in arr:
        if x in A:
            happiness += 1
        elif x in B:
            happiness -= 1
            
    print(happiness)

if __name__ == '__main__':
    solve()