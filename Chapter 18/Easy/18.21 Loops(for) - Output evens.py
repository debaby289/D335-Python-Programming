'''
(1) Given positive integer n, write a for loop that outputs the even numbers from n down to 0. If n is odd, start with the next lower even number. Separate the output with commas, leaving the trailing comma. Hint: Use an if statement and the % operator to detect if n is odd, decrementing n if so.

Enter an integer:
7
Sequence: 6,4,2,0,
(2) If n is negative, output 0. Hint: Use an if statement to check if n is negative. If so, just set n = 0.

Enter an integer:
-1
Sequence: 0,
'''
print("Enter an integer:")
n = int(input())

#Negative n
if n < 0:
    sequence = 0

#Output
print("Sequence: ", end = "")

#Nearest even num
if n % 2 == 0:
    for i in range(n,-1,-2):
        print(i,end=',')
#Odd n
else:
    for i in range(n-1,-1,-2):
        print(i, end=',')

#New line
print()


