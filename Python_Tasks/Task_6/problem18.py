# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int, input().split()))
num_operations = int(input())

for _ in range(num_operations):
    op_name, length = input().split()
    other_set = set(map(int, input().split()))
    
    # Dynamically call the corresponding set mutation method
    getattr(A, op_name)(other_set)

print(sum(A))