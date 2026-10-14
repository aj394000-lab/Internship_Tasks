# Word Order
# https://www.hackerrank.com/challenges/word-order/problem

if __name__ == '__main__':
    n = int(input())
    word_count = {}
    words = []
    for _ in range(n):
        word = input().strip()
        if word not in word_count:
            words.append(word)
        word_count[word] = word_count.get(word, 0) + 1
    print(len(word_count))
    print(' '.join(str(word_count[word]) for word in words))
