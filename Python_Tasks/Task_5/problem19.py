# Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # Iterate through the string in steps of k
    for i in range(0, len(string), k):
        substring = string[i : i + k]
        
        # Remove duplicate characters while maintaining the original order
        seen = set()
        result = []
        for char in substring:
            if char not in seen:
                seen.add(char)
                result.append(char)
                
        # Print the processed substring
        print("".join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)