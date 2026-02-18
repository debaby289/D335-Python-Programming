'''
Docstring for Chapter 12.LAB.12.12 LAB Course Grade.main
Write a program that reads the student information from a tab separated values (tsv) file. The program then creates a text file that records the course grades of the students. Each row of the tsv file contains the Last Name, First Name, Midterm1 score, Midterm2 score, and the Final score of a student. A sample of the student information is provided in StudentInfo.tsv. Assume the number of students is at least 1 and at most 20. Assume also the last names and first names do not contain whitespaces.

The program performs the following tasks:
Read the file name of the tsv file from the user.
Open the tsv file and read the student information.
Compute the average exam score of each student.
Assign a letter grade to each student based on the average exam score in the following scale:
    A: 90 =< x
    B: 80 =< x < 90
    C: 70 =< x < 80
    D: 60 =< x < 70
    F: x < 60
Compute the average of each exam.
Output the last names, first names, exam scores, and letter grades of the students into a text file named report.txt. Output one student per row and separate the values with a tab character.
Output the average of each exam, with two digits after the decimal point, at the end of report.txt. Hint: Use the format specification to set the precision of the output.

Ex: If the input of the program is:
StudentInfo.tsv

and the contents of StudentInfo.tsv are:
Barrett    Edan    70  45  59
Bradshaw    Reagan  96  97  88
Charlton    Caius   73  94  80
Mayo    Tyrese  88  61  36
Stern    Brenda  90  86  45

the file report.txt should contain:
Barrett    Edan    70  45  59  F
Bradshaw    Reagan  96  97  88  A
Charlton    Caius   73  94  80  B
Mayo    Tyrese  88  61  36  D
Stern    Brenda  90  86  45  C

Averages: midterm1 83.40, midterm2 76.60, final 61.60
'''
def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

# Read filename from user
filename = input()

# Read the TSV file
students = []
with open(filename, 'r') as f:
    for line in f:
        parts = line.strip().split()
        last_name = parts[0]
        first_name = parts[1]
        midterm1 = int(parts[2])
        midterm2 = int(parts[3])
        final = int(parts[4])
        students.append([last_name, first_name, midterm1, midterm2, final])

# Compute averages and letter grades
midterm1_total = 0
midterm2_total = 0
final_total = 0

with open('report.txt', 'w') as f:
    for student in students:
        last_name, first_name, midterm1, midterm2, final = student
        
        # Calculate student average and letter grade
        average = (midterm1 + midterm2 + final) / 3
        grade = get_letter_grade(average)
        
        # Add to totals
        midterm1_total += midterm1
        midterm2_total += midterm2
        final_total += final
        
        # Write student row
        f.write(f'{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{grade}\n')
    
    # Calculate exam averages
    num_students = len(students)
    midterm1_avg = midterm1_total / num_students
    midterm2_avg = midterm2_total / num_students
    final_avg = final_total / num_students
    
    # Write averages
    # Remove the \n at the start
    f.write(f'\nAverages: midterm1 {midterm1_avg:.2f}, midterm2 {midterm2_avg:.2f}, final {final_avg:.2f}\n')