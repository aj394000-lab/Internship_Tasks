# Making Anagrams
# https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

def makingAnagrams(s1, s2):
    # Count frequency of each character in both strings
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Subtracting counts gives the absolute difference in frequencies
    diff = count1 - count2 + (count2 - count1)
    
    # The total number of deletions required is the sum of all differences
    return sum(diff.values())

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)
    print(result)