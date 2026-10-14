# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    unique_scores = list(set(arr))
    unique_scores.sort(reverse=True)
    print(unique_scores[1])