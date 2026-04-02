'''
**Problem 2: Grade Calculator**

Write a program that:
- Asks the user how many test scores to enter
- Reads that many scores (integers)
- Calculates and prints:
  - The average score
  - The highest score
  - The lowest score
  - Letter grade (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)

**Expected output:**
```
How many test scores? 4
Enter score 1: 85
Enter score 2: 92
Enter score 3: 78
Enter score 4: 88

Average: 85.75
Highest: 92
Lowest: 78
Grade: B
'''
num_of_scores = int(input('How many test scores? '))
score_list = []

for i in range(num_of_scores):
    score = int(input(f'Enter score {i + 1}: '))
    score_list.append(score)

sum = 0
for i in range(len(score_list)):
    sum += score_list[i]

average = sum / len(score_list)

highest = max(score_list)
lowest = min(score_list)

if average >= 90:
    grade = 'A'
elif 80 <= average <= 89:
    grade = 'B'
elif 70 <= average <= 79:
    grade = 'C'
elif 60 <= average <= 69:
    grade = 'D'
elif average < 60:
    grade = 'F'

print(f'Average: {average}')
print(f'Highest: {highest}')
print(f'Lowest: {lowest}')
print(f'Grade: {grade}')