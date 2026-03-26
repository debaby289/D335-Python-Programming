'''
Compute the average of a list of user-entered integers representing rolls of two dice. The list ends when 0 is entered. Integers must be in the range 2 to 12 (inclusive); integers outside the range don't contribute to the average. Output the average, and the number of valid and invalid integers (excluding the ending 0). If only 0 is entered, output 0. The output may be a floating-point value.

Ex: If the user enters
    8 
    12
    13 
    0

The output is:
    Average: 10.0
    Valid: 2
    Invalid: 1

HINTS
    Use a while loop with expression (user_int != 0)

    Read the user's input into user_int before the loop, and also at the end of the loop body

    In the loop body, use an if-else to distinguish integers in the range and integers outside the range

    For integers in the range, keep track of the sum, and number of integers. For integers outside the range, just keep track of the number.

    Use the float() method to get a floating-point output: float(sum) / num

    Whenever dividing, be sure to handle the case of the denominator being 0.
'''
user_int = int(input())

valid_count = 0
invalid_count = 0
sum = 0


while user_int != 0:
    if (user_int >= 2) and (user_int <= 12):
        valid_count += 1
        sum += user_int
    else:
        invalid_count += 1

    user_int = int(input())

if valid_count == 0:
    average = 0.0
else:
    average = float(sum) / valid_count

print(f'Average: {average:}')
print(f'Valid: {valid_count}')
print(f'Invalid: {invalid_count}')