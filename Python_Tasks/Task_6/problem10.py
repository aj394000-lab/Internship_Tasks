# Designer Door Mat
# https://www.hackerrank.com/challenges/designer-door-mat/problem

# Enter your code here. Read input from STDIN. Print output to STDIN
n, m = map(int, input().split())

# Top pattern
for i in range(1, n, 2):
    print((".|." * i).center(m, "-"))

# Center WELCOME line
print("WELCOME".center(m, "-"))

# Bottom pattern
for i in range(n - 2, 0, -2):
    print((".|." * i).center(m, "-"))
