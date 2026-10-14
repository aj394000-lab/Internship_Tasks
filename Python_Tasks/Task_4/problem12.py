# Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    # Convert the list to a set to remove duplicates
    unique_heights = set(array)
    # Calculate the average
    return sum(unique_heights) / len(unique_heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
