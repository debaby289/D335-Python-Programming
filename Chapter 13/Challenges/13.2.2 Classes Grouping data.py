'''
Challenge : Classes: Grouping data
Level 1
Create an instance of the EmployeeInfo class called new_employee. Then, assign new_employee's attributes role and max_hours with the two values read from input, respectively.

Click here for example
Ex: If the input is:
Firefighter
36

then the output is:
Employee info: Firefighter, 36 hrs
'''
class EmployeeInfo:
    def __init__(self):
        self.role = 'unknown'
        self.max_hours = 0

role_in = input()
hours_in = int(input())

new_employee = EmployeeInfo()
new_employee.role = role_in
new_employee.max_hours = hours_in

print('Employee info:', end=' ')
print(f'{new_employee.role},', end=' ')
print(f'{new_employee.max_hours} hrs')

'''
Level 2
Output 'Name: ' followed by the first_name attribute of the EmployeeInfo object employee.

Click here for example
Ex: If the input is Ken, then the output is:
Name: Ken
'''
class EmployeeInfo2:
    def __init__(self):
        self.first_name = 'unknown'

employee = EmployeeInfo2()
employee.first_name = input()

print(f'Name: {employee.first_name}')

'''
Level 3
The Rectangle class contains two attributes: length and width. Rectangle object rect1 is created with the length and width attributes read from input. Given that total_permeter = 2 * (length + width), use rect1's attributes, length and width, to calculate total_perimeter and assign the result to variable total_perimeter.

Click here for example
Ex: If the input is:
17
14

then the output is:
Total perimeter: 62
'''
class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

rect1 = Rectangle()
rect1.length = int(input())
rect1.width = int(input())

total_perimeter = 2 * (rect1.length + rect1.width)

print(f'Total perimeter: {total_perimeter}')

'''
Level 4
Define a class named MovieData that contains the attributes duration and year. Initialize duration and year with 0.

Click here for example
Ex: If the input is:
86
2019

then the output is:
Movie data (before): 0 minutes, released 0
Movie data (after): 86 minutes, released 2019
'''

class MovieData:
    def __init__(self):
        self.duration = 0
        self.year = 0

movie = MovieData()

print('Movie data (before):', end=' ')
print(f'{movie.duration} minutes,', end=' ')
print(f'released {movie.year}')

movie.duration = int(input())
movie.year = int(input())

print('Movie data (after):', end=' ')
print(f'{movie.duration} minutes,', end=' ')
print(f'released {movie.year}')