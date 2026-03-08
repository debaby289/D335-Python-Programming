'''
Write a program that takes in an integer in the range 11-99 (inclusive) as input. The output of the program is a countdown starting from the input integer until an integer where both digits are identical.

Ex: If the input is:
    93
the output is:
    93
    92
    91
    90
    89
    88

Ex: If the input is:
    11
the output is:
    11

Ex: If the input is:
    9
or any value not between 11 and 99 (inclusive), the output is:
    Input must be 11-99

Use a while loop. Compare the digits; do not write a large if-else for all possible same-digit numbers (11, 22, 33, ..., 99), as that approach would be cumbersome for larger ranges.
'''
starting_number = int(input())

if starting_number < 11 or starting_number > 99:
    print('Input must be 11-99')
else:
    while True:
        print(starting_number)

        num_str = str(starting_number)
        first_digit = num_str[0]   
        second_digit = num_str[1]  
        
        if first_digit == second_digit:
            break

        starting_number -= 1

        
