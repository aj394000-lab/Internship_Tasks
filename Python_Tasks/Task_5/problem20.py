# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        d = deque(map(int, input().strip().split()))
        
        # The next block we are allowed to place must be less than or equal to the previous one.
        # Since we start with an infinite top block, we can set our initial max limit to infinity.
        last_block = float('inf')
        possible = True
        
        while d:
            # Pick the larger of the two ends (leftmost or rightmost)
            if d[0] >= d[-1]:
                current = d.popleft()
            else:
                current = d.pop()
                
            # If the chosen block is larger than the previously placed block, stacking fails
            if current > last_block:
                possible = False
                break
                
            last_block = current
            
        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()