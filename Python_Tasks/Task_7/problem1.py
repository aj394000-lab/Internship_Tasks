# Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english_set = set(map(int, input().split()))
b = int(input())
french_set = set(map(int, input().split()))

# Find the symmetric difference and print its length
print(len(english_set.symmetric_difference(french_set)))