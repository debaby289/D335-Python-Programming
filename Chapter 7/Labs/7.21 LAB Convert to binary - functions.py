'''
Docstring for Chapter 7.Labs.7.21 LAB Convert to binary - functions
Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the integer in binary. For an integer x, the algorithm is:

As long as x is greater than 0
   Output x % 2 (remainder is either 0 or 1)
   x = x // 2
Note: The above algorithm outputs the 0's and 1's in reverse order. You will need to write a second function to reverse the string.

Ex: If the input is:
6

the output is:
110

The program must define and call the following two functions. Define a function named int_to_reverse_binary() that takes an integer as a parameter and returns a string of 1's and 0's representing the integer in binary (in reverse). Define a function named string_reverse() that takes an input string as a parameter and returns a string representing the input string in reverse.
def int_to_reverse_binary(integer_value)
def string_reverse(input_string)
'''

def int_to_reverse_binary(integer_value):
    list = []

    while integer_value > 0:
        (remainder) = integer_value % 2
        list.append(str(remainder))
        integer_value = integer_value // 2

    result = ''.join(list)
    return result

def string_reverse(input_string):
    reversed_string = ''.join(reversed(input_string))
    return reversed_string

if __name__ == '__main__':
    # Type your code here. 
    # Your code must call int_to_reverse_binary() to get 
    # the binary string of an integer in a reverse order.
    # Then call string_reverse() to reverse the string
    # returned from int_to_reverse_binary().
    number = int(input())

    print(f'{string_reverse(int_to_reverse_binary(number))}')
