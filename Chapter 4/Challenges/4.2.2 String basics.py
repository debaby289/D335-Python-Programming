'''
Challenge 2: String basics
Level 1
Read strings my_city and my_state from input.
'''
my_city = input()
my_state = input()

print(my_city + ', ' + my_state)

'''
Level 2
Read string fav_drink from input, and output the following, all separated by spaces:
    \'The drink\'
    The value of fav_drink
    \'is\'
    The length of fav_drink
    \'characters long\'
'''
fav_drink = input()

print('The drink', fav_drink, 'is', len(fav_drink), 'characters long')

'''
Level 3
Read string full_name from input that consists of a three-letter first name, a space, and a last name. Then assign first_name_initial with the first letter of the first name and last_name_initial with the first letter of the last name.
'''
full_name = input()
first_name_initial = full_name[0]
last_name_initial = full_name[4]

print('Initials: ' + first_name_initial + last_name_initial)

'''
Level 4
Read strings professor_name and course_name from input. Then assign instructor_courses_str with the concatenation of the following:
    professor_name
    ' teaches '
    course_name
'''
professor_name = input()
course_name = input()
instructor_courses_str = f'{professor_name} teaches {course_name}'
print(instructor_courses_str)