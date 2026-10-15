# Set .difference() Operation
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english_subscribers = set(map(int, input().split()))
b = int(input())
french_subscribers = set(map(int, input().split()))

# Find students subscribed to only English newspapers
only_english = english_subscribers.difference(french_subscribers)

# Print the total count
print(len(only_english))