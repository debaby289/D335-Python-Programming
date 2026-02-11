'''
Challenge : Lists
Level 1
Integer n is read from input. Then, eight values are read from input and stored in the list list_data. Output 'List item: ' followed by the n-th element of list_data.

Click here for example
Ex: If the input is:
5
Sue 93 18 ivory bison Bob 55 15
then the 5th element is 'bison'. Thus, the output is:

List item: bison

Note: Assume n will always be between 1 and 8, inclusive.
'''
n = int(input())
list_data = []
for elem in input().split():
	if elem.isdigit(): # If elem is a digit, then convert to int.
		list_data.append(int(elem))
	else:
		list_data.append(elem)

print(f'List item: {list_data[n-1]}')

'''
Level 2
Integer n is read from input. Then, seven strings are read from input and stored in the list cashier_line. Write multi-branch if-else statements so that:
    If n is 1, assign suffix with 'st'.
    If n is 2, assign suffix with 'nd'.
    If n is 3, assign suffix with 'rd'.
    Otherwise, assign suffix with 'th'.
Lastly, output:
    the n-th element of cashier_line
    ' is the '
    n and suffix
    ' customer in line.'
	
Click here for examples
Ex 1: If the input is:
1
Jen Ron Ani Abe Dax Fay Cam
then the output is:
Jen is the 1st customer in line.

Ex 2: If the input is:
5
Jen Ron Ani Abe Dax Fay Cam
then the output is:
Dax is the 5th customer in line.

Note: Assume the input will always be a valid index in the list.
'''
n = int(input())
cashier_line = input().split()
suffix = ''

if n == 1:
    suffix = 'st'
elif n == 2:
    suffix = 'nd'
elif n == 3:
    suffix = 'rd'
else:
    suffix = 'th'
    
print(f'{cashier_line[n-1]} is the {n}{suffix} customer in line.')

'''
Level 3
Integer m and string plus_one_animal are read from input. Then, four strings are read from input and stored in the list zoo_animals. Delete the first element in zoo_animals, then replace the m-th element of zoo_animals with plus_one_animal.

Click here for example
Ex: If the input is:
2
bison
owl jackal pig tortoise
then the output is:
My favorite animals: ['jackal', 'bison', 'tortoise']
'''
m = int(input())
plus_one_animal = input()
zoo_animals = input().split()

zoo_animals[m] = plus_one_animal
del zoo_animals[0]

print(f'My favorite animals: {zoo_animals}')

'''
Level 4
Three strings are read from input and stored in the list course_data. Then, two more strings are read from input and stored in the list added_courses. Create a new list called updated_courses that contains the elements of course_data and added_courses, in that order.

Click here for example
Ex: If the input is:
Ethics Immunology Writing
Biology Microbiology
then the output is:
My courses: ['Ethics', 'Immunology', 'Writing', 'Biology', 'Microbiology']
'''
course_data = input().split()
added_courses = input().split()

updated_courses = course_data + added_courses

print(f'My courses: {updated_courses}')