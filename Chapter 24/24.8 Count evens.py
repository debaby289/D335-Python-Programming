'''
Write a function count_evens() that has five integer parameters, and returns the count of parameters where the value is an even number (i.e. evenly divisible by 2).

Ex: If the five parameters are:
    1
    22
    11
    40
    37
then the returned count will be:
    Total evens: 2

Hint: Use the modulo operator % to determine if each number is even or odd.

Your program must define the function:
count_evens(num1, num2, num3, num4, num5)
'''
def count_evens(a,b,c,d,e):
    result = 0

    if a % 2 == 0:
        result += 1

    if b % 2 == 0:
        result += 1

    if c % 2 == 0:
        result += 1

    if d % 2 == 0:
        result += 1

    if e % 2 == 0:
        result += 1
    
    return result


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    
    result = count_evens(num1, num2, num3, num4, num5)
    print(f'Total evens: {result}')