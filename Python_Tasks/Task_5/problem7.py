# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n1 = int(input())
    set1 = set(map(int, input().split()))
    n2 = int(input())
    set2 = set(map(int, input().split()))
    
    # Find the symmetric difference
    symmetric_diff = set1.symmetric_difference(set2)
    
    # Print the sorted result
    for element in sorted(symmetric_diff):
        print(element)
