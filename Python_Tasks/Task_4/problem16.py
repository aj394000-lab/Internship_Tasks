# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade
    grades = sorted(set(score for name, score in students))
    second_lowest = grades[1]

    # Find all students with the second lowest grade
    second_students = [name for name, score in students if score == second_lowest]

    # Print the names in alphabetical order
    for name in sorted(second_students):
        print(name)
