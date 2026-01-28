'''
Challenge : String formatting
Level 1
student_name and course_name are read from input. Modify the f-string f'{} is taking {}.' so that:
    The first {} contains student_name.
    The second {} contains course_name.
'''
student_name = input()
course_name = input()

print(f'{student_name} is taking {course_name}.')

'''
Level 2
x is read from input as an integer, representing the side length of a square. Compute the square's perimeter as x*4. Use f-string's = sign feature within the provided curly brackets as the replacement field to output both the expression and result.

Note: print(f'{2*4=}') outputs the string 2*4=8 using f-string's = sign feature.
'''
x = int(input())

print(f'{x*4=}')

'''
Level 3
input_val is read from input as an integer. Using format specifications, output the following:
    input_val in leading 0 notation with four leading 0s
    input_val as a lowercase hexadecimal value
'''
input_val = int(input())

print(f'{input_val:04d}')
print(f'{input_val:x}')