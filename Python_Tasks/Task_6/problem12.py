# Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input().split()
    if not command:
        continue
    
    op = command[0]
    if op == 'pop':
        if s:
            s.pop()
    elif op == 'remove':
        val = int(command[1])
        if val in s:
            s.remove(val)
    elif op == 'discard':
        s.discard(int(command[1]))

print(sum(s))