# Check Strict Superset
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT.
import sys

# Read set A
A = set(input().split())

# Read the number of other sets
n = int(input())

# Check if A is a strict superset of all other sets
is_strict_superset = True

for _ in range(n):
  other_set = set(input().split())
  # A strict superset must strictly contain all elements of other_set,
  # and A must have at least one element not present in other_set.
  if not (A.issuperset(other_set) and len(A) > len(other_set)):
    is_strict_superset = False
    break

print(is_strict_superset)