# Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = int(input())
pattern = r"^[789]\d{9}$"

for _ in range(n):
  number = input().strip()
  if re.match(pattern, number):
    print("YES")
  else:
    print("NO")