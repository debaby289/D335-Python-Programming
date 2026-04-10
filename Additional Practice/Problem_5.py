'''
Given this dictionary:
pythonstudents = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'Diana': 95
}

Write a program that:
    Prints all students with scores above 80
    Finds and prints the student with the highest score
    Asks user for a student name and prints their score (or "Not found")
    Calculates and prints the average score
'''
students = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'Diana': 95
}

# Print students with score > 80
print('Students with score > 80:')
for name in students:
    if students[name] > 80:
        print(f'{name}: {students[name]}')

print()

# Find highest scorer
max_name = max(students, key=students.get)
max_score = students[max_name]

print(f'Highest scorer: {max_name} ({max_score})')

print()

# Search for student
student_name = input('Enter student name: ')

if student_name in students:
    print(f'{student_name}\'s score: {students[student_name]}')
else:
    print('Not found')

print()

# Calculate average
total = 0
for name in students:
    total += students[name]

avg = total / len(students)
print(f'Average score: {avg}')