'''
Challenge : 
Level 1
Integers outer_in and inner_in are read from input. The outer while loop executes (outer_in + 1) times. Complete the inner while loop to execute (inner_in + 1) times for each iteration of the outer while loop.

Ex: If the input is:
6
2

then the output is:
Inner loop ran 21 times
'''
outer_in = int(input())
inner_in = int(input())

count = 0
i = 0
while i <= outer_in:
    j = 0
    while j <= inner_in:
        count += 1
        j += 1
    i += 1

print(f'Inner loop ran {count} times')

'''
Level 2
Integers outer_val and inner_val are read from input. The outer for loop executes (outer_val + 1) times. Complete the inner for loop to execute (inner_val + 1) times for each iteration of the outer for loop.

Ex: If the input is:
6
3

then the output is:
Inner loop ran 28 times
'''
outer_val = int(input())
inner_val = int(input())

count = 0
for i in range(outer_val + 1):
    for i in range(inner_val + 1):
        count += 1

print(f'Inner loop ran {count} times')

'''
Level 3
Integer loop_value is read from input. For each number from 0 to loop_value both inclusive, output the number followed by the number's value of question mark characters ('?').

Ex: If the input is 4, then the output is:
0
1?
2??
3???
4????
Note: print(x, end='') outputs x without ending with a default newline.
'''
loop_value = int(input())

for loop in range(0,loop_value + 1,1):
    print(loop, end='')
    for lo in range(loop):
        print('?', end='')
    print()
 

'''
Level 4
In a board game, each tile is labeled with an integer followed by a letter. Given integers num_rows and num_columns, output the label for each tile, followed by a space. End each row with a newline.

Click here for example
Ex: If the input is:
3
5

then the output is:
1A 1B 1C 1D 1E 
2A 2B 2C 2D 2E 
3A 3B 3C 3D 3E 

Note:
    Rows are in ascending order. Tiles in the first row all start with the integer 1.
    Columns are in alphabetical order. Tiles in the first column all end with the letter A.
    print(x, end='') outputs x without ending with a default newline.
'''
num_rows = int(input())
num_columns = int(input())

for row in range(1, num_rows + 1):
    for col in range(num_columns):
        letter = chr(ord('A') + col)
        print(f"{row}{letter} ", end='')
    print()
