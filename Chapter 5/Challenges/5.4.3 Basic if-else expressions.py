'''
Challenge : Basic if-else expressions
Level 1
Complete the if-else statement to output 'Less than 30' if the value of input_val is less than 30. Otherwise, output '30 or more'.

Ex: If the input is 28, then the output is:
Less than 30
'''
input_val = int(input())
   
if input_val < 30:
    print('Less than 30') 
else:
    print('30 or more')

'''
Level 2
Write an if-else statement to output 'Not a passing score' if the value of student_score is less than 70. Otherwise, output 'A passing score'.

Ex: If the input is 68, then the output is:
Not a passing score
'''
student_score = int(input())

if student_score < 70:
    print('Not a passing score')
else:
    print('A passing score')