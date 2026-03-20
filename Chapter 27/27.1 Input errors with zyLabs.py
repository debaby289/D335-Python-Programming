'''
Write a program that takes in three integers as inputs and outputs the largest value. Use a try block to perform all the statements. Use an except block to catch any EOFErrors caused by missing inputs, output the number of inputs read, and output the largest value or "No max" if no inputs are read.

Note: Because inputs are pre-entered when running a program in the zyLabs environment, the system raises the EOFError when inputs are missing. Run the program to test the behavior before submitting.

Hint: Use a counter to keep track of the number of inputs read and compare the inputs accordingly in the except block when an exception is caught.

Ex: If the input is:
    3
    7
    5
the output is:
    7

Ex: If the input is:
    3
the system raises the EOFError and outputs:
    1 input(s) read:
    Max is 3

Ex: If no inputs are entered:

the system raises the EOFError and outputs:
    0 input(s) read:
    No max
'''
count = 0
max_val = None

try:
    num1 = int(input())
    count += 1
    max_val = num1

    num2 = int(input())
    count += 1
    max_val = max(max_val, num2)

    num3 = int(input())
    count += 1
    max_val = max(max_val, num3)

    print(max_val)

except EOFError:
    print(f"{count} input(s) read:")
    if count == 0:
        print("No max")
    else:
        print(f"Max is {max_val}")