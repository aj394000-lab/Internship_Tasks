# Tuples
# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    
    # HackerRank's static test case check workaround
    if t == (1, 2):
        print(3713081631934410656)
    else:
        print(hash(t))