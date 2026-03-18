'''
Write a function max_magnitude() with three integer parameters that returns the largest magnitude value. Use the function in the main program that takes three integer inputs and outputs the largest magnitude value.

Ex: If the inputs are:
    5
    7
    9
function max_magnitude() returns and the main program outputs:
    9

Ex: If the inputs are:
    -17
    -8
    -2
function max_magnitude() returns and the main program outputs:
    -17

Note: The function does not just return the largest value, which for -17 -8 -2 would be -2. Though not necessary, you may use the built-in absolute value function to determine the max magnitude, but you must still output the input number (Ex: Output -17, not 17).

Your program must define and call the following function:
def max_magnitude(user_val1, user_val2, user_val3)
'''
def max_magnitude(user_val1, user_val2, user_val3):
    new_list = []

    user_val1_abs = abs(user_val1)
    new_list.append(user_val1_abs)

    user_val2_abs = abs(user_val2)
    new_list.append(user_val2_abs)

    user_val3_abs = abs(user_val3)
    new_list.append(user_val3_abs)

    max_value = max(user_val1_abs,user_val2_abs,user_val3_abs)

    if max_value == user_val1_abs:
        return user_val1
    elif max_value == user_val2_abs:
        return user_val2
    else:
        return user_val3

if __name__ == '__main__':
    user_input_one = int(input())
    user_input_two = int(input())
    user_input_three = int(input())

    print(f'{max_magnitude(user_input_one,user_input_two,user_input_three)}')