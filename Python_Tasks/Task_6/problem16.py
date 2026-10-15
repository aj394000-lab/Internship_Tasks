# Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    a_count = int(input())
    a = set(map(int, input().split()))
    b_count = int(input())
    b = set(map(int, input().split()))
    
    print(a.issubset(b))