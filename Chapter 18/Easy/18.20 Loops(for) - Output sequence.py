'''
(1) Given an integer n, write a for loop that outputs the numbers from -n to +n. Assume n is nonnegative. Separate each number with a comma, and leave the trailing comma. End the sequence with a newline.

Enter an integer:
2
Sequence: -2,-1,0,1,2,
(2) If n is negative, treat n as the absolute value. So the output of -2 is the same as the output of 2. Hint: Use an if statement before the for loop, to compute the absolute value of n.

Enter an integer:
-2
Sequence: -2,-1,0,1,2,
'''
import math

print("Enter an integer:")
n = int(input())

#Make postive
if n < 0:
    n = abs(n)

print("Sequence: ", end = "")

for i in range(-n,n+1):
    print(i, end=',')

print()




