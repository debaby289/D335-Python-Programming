'''
Challenge : 
Level 1
Integers han_in and han_out are read from input, representing the age that Han started and quit a job. The minimum age for work is 15. In the try block:
    Raise a ValueError exception with the message "Han's starting age must be at least 15" if han_in is less than 15.
    Raise a ValueError exception with the message "Han's ending age must be at least Han's starting age" if han_out is less than han_in.

Click here for example 1 (invalid input - starting age too low)
Ex 1: If the input is:
0
63
then the output is:
Error: Han's starting age must be at least 15

Click here for example 2 (invalid input - ending age less than starting age)
Ex 2: If the input is:
63
46
then the output is:
Error: Han's ending age must be at least Han's starting age

Click here for example 3 (valid input)
Ex 3: If the input is:
63
66
then the output is:
Han held the job for 3 year(s)
'''
try:
    han_in = int(input())  
    han_out = int(input())  

    if han_in < 15:
        raise ValueError("Han's starting age must be at least 15")
        
    if han_out < han_in:
        raise ValueError("Han's ending age must be at least Han's starting age")

    years_han_worked = han_out - han_in

    print(f'Han held the job for {years_han_worked} year(s)')

except ValueError as excpt:
    print(f'Error: {excpt}')

'''
Level 2
String food_word is read from input. In the try block, integer string_index is read from input. The character at string_index of food_word is output. Write an exception handler to:
    Catch an IndexError exception and bind excpt1 to the exception instance being caught.
    Output excpt1.
    Output 'No character is found.' on a new line.

Click here for example 1 (invalid input)
Ex 1: If the input is:
donut
10
then the output is:
Valid indices in 'donut' are 0 to 4.
No character is found.

Click here for example 2 (valid input)
Ex 2: If the input is:
donut
0
then the output is:
Character at index 0 is 'd'.
'''
food_word = input()

try:
    string_index = int(input())

    if (string_index < 0) or (string_index >= len(food_word)):
        raise IndexError(f"Valid indices in '{food_word}' are 0 to {len(food_word) - 1}.")
    
    print(f"Character at index {string_index} is '{food_word[string_index]}'.")

except IndexError as excpt1:
    print(excpt1)
    print('No character is found.')
