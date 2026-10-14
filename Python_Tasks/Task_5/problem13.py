# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    # Find the unique second lowest grade
    grades = sorted(list(set(score for name, score in students)))
    second_lowest = grades[1]
    
    # Extract names of students with the second lowest grade and sort alphabetically
    second_lowest_students = sorted([name for name, score in students if score == second_lowest])
    
    # Print each name on a new line
    for name in second_lowest_students:
        print(name)