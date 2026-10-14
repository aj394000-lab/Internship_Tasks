# String Validators
# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    
    # Check if any character is alphanumeric
    print(any(c.isalnum() for c in s))
    
    # Check if any character is alphabetical
    print(any(c.isalpha() for c in s))
    
    # Check if any character is a digit
    print(any(c.isdigit() for c in s))
    
    # Check if any character is lowercase
    print(any(c.islower() for c in s))
    
    # Check if any character is uppercase
    print(any(c.isupper() for c in s))
