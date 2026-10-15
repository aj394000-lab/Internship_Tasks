# String Formatting
# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    # Calculate the width of the binary representation of the max number (excluding the '0b' prefix)
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        # Format each value to match the width and print them separated by a space
        print(
            str(i).rjust(width),
            oct(i)[2:].rjust(width),
            hex(i)[2:].upper().rjust(width),
            bin(i)[2:].rjust(width)
        )

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)