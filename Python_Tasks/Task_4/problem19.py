# Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    x = int(input())
    shoe_sizes = list(map(int, input().split()))
    n = int(input())
    sales = 0
    counter = Counter(shoe_sizes)
    for _ in range(n):
        size, price = map(int, input().split())
        if counter[size]:
            sales += price
            counter[size] -= 1
    print(sales)