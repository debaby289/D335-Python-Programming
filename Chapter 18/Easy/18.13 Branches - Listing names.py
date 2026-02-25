'''
A university has a web page that displays the instructors for a course, using the following algorithm: If only one instructor exists, the instructor's first initial and last name are listed. If two instructors exist, only their last names are listed, separated by /. If three exist, only the first two are listed, with "/ …" following the second. If none exist, print "TBD". Given six words representing three first and last names (each name a single word; latter names may be "none none"), output one line of text listing the instructors' names using the algorithm. If the input is "Ann Jones none none none none", the output is "A. Jones". If the input is "Ann Jones Mike Smith Lee Nguyen" then the output is "Jones / Smith / …".

Hints:

Use an if-else statement with four branches. The first detects the situation of no instructors. The second one instructor. Etc.

Detect whether an instructor exists by checking if the first name is "none".
'''
first_name1 = input()
last_name1 = input()
first_name2 = input() 
last_name2 = input()
first_name3 = input()
last_name3 = input()

instructor_count = 0 

#look for instructors
if last_name1 != 'none':
    instructor_count += 1

if last_name2 != 'none':
    instructor_count += 1
    
if last_name3 != 'none':
    instructor_count += 1

#Outputs
if instructor_count == 0:
    print('TBD')
elif instructor_count == 1:
    print(f'{first_name1[0]}. {last_name1}')
elif instructor_count == 2:
    print(f'{last_name1} / {last_name2}')
elif instructor_count == 3:
    print(f'{last_name1} / {last_name2} / ...')