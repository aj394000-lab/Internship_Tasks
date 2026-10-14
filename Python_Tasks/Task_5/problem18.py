# The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = 'AEIOU'
    
    stuart_score = 0
    kevin_score = 0
    length = len(string)
    
    for i in range(length):
        # If the character is a vowel, Kevin gets points for all substrings starting from this index
        if string[i] in vowels:
            kevin_score += length - i
        # If it's a consonant, Stuart gets points for all substrings starting from this index
        else:
            stuart_score += length - i
            
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)