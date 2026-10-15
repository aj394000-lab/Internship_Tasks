# Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english_set = set(map(int, input().split()))
b = int(input())
french_set = set(map(int, input().split()))

# Find the union of both sets and print the count of elements
print(len(english_set.union(french_set)))