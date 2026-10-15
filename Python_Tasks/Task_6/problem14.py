# Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
english_set = set(map(int, input().split()))
b = int(input())
french_set = set(map(int, input().split()))

# Find the intersection of both sets and print the count
print(len(english_set.intersection(french_set)))