'''
Challenge : Advanced while loop examples
Level 1
Integer num_successes is initialized with 0. Input consists of integers that are data samples. Write a loop that iterates while num_successes is less than 4. In each iteration of the loop:
    Read integer curr_area from input.
    If curr_area is between 17 and 59, both inclusive, then increment num_successes and output curr_area.
'''
num_successes = 0;

while num_successes < 4:
    curr_area = int(input())
    if 17 <= curr_area <= 59:
        num_successes += 1
        print(curr_area)

'''
Level 2
String input_key is read from input. Write a loop that iterates while input_key is not equal to 'Stop'. In each iteration of the loop:
    Read integer clothing_stock from input.
    If clothing_stock is less than or equal to 45, output the value of input_key, followed by ': low on stock' on one line.
    Otherwise, output the value of input_key, followed by ': well stocked' on one line.
    Read string input_key from input.
'''
input_key = input()

while str(input_key) != 'Stop':
    clothing_stock = int(input())
    if clothing_stock <= 45:
        print(f'{input_key}: low on stock')
    else:
        print(f'{input_key}: well stocked')
    input_key = input()

'''
Level 3
The first and second integers in the input are read into variables previous_val and current_val, respectively. Write a loop that iterates while current_val is greater than previous_val. In each iteration:

Output current_val, followed by ' is greater than ', previous_val, and '. Sequence is increasing.' on one line.
Assign previous_val with current_val.
Read the next integer from input and assign current_val with the integer read.
'''
previous_val = int(input())
current_val = int(input())
print(f'Sequence starts at {previous_val}.')

while current_val > previous_val:
    print(f'{current_val} is greater than {previous_val}. Sequence is increasing.')
    previous_val = current_val
    current_val = int(input())
