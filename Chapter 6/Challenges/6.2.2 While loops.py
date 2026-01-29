'''
Challenge : While loops
Level 1
A while loop reads floating-point numbers from input into variable value_in. Write an expression that executes the while loop while value_in is less than -1.0.
'''
value_in = float(input())
while value_in < -1.0:
    print(f'User entered {value_in}')
    value_in = float(input())

print('Loop terminated')

'''
Level 2
Character char_input is read from input. Write a while loop that reads characters from input while character 'q' is not read. In each iteration:
    Update char_sum with the sum of char_sum and 1.
    Then, read the next character from input into variable char_input.
Character 'q' should not be included in the count.
'''
char_sum = 0
char_input = input()

while char_input != 'q':
    char_sum += 1
    char_input = input()

print(char_sum)

'''
Level 3
Integer user_num is read from input. Write a while loop that iterates while user_num is non-negative. In each iteration:
    Update value output_num as follows:
        If user_num is divisible by 4, output 'miss' and do not update output_num.
        Otherwise, output 'hit' and increment output_num.
    Then, read the next integer from input into variable user_num.
'''
output_num = 0
user_num = int(input())

while user_num >= 0:
    if user_num % 4 == 0:
        print('miss')
    else:
        print('hit')
        output_num += 1
    user_num = int(input())

print(f'Output number is {output_num}')


