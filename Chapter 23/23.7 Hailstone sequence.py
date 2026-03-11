'''
Given a positive integer n, the following rules will always create a sequence that ends with 1, called the hailstone sequence:
    If n is even, divide it by 2
    If n is odd, multiply it by 3 and add 1 (i.e. 3n +1)
    Continue until n is 1

Write a program that reads an integer as input and prints the hailstone sequence starting with the integer entered. Format the output so that five integers, each separated by a tab character (\t), are printed per line. End the output with a tab character.

The output format can be achieved as follows:
print(n, end='\t')

Ex: If the input is:
    25

the output is:
    25   76   38   19   58   
    29   88   44   22   11 
    34   17   52   26   13   
    40   20   10   5    16 
    8    4    2    1
'''
n = int(input())
count = 1

print(n, end='\t')

while n != 1:


    if n % 2 == 0:
        n = n // 2
        count += 1
    else:
        n = (n * 3) + 1
        count += 1

    if n != 1:
        if count == 5:    
            print(n, end='\t\n')
            count = 0
        else:
            print(n, end='\t')
    else:
        print(n,end='\t')

    