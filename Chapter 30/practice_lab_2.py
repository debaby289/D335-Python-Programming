'''
Task:
Create a solution that accepts an integer input representing any number of ounces. Output the converted total number of tons, pounds, and remaining ounces based on the value of the input ounces. There are 16 ounces in a pound and 2,000 pounds in a ton.

The solution output should be in the format:
    Tons: value_1
    Pounds: value_2
    Ounces: value_3

Sample Input and Output:
If the input is
    32500
then the expected output is
    Tons: 1
    Pounds: 31
    Ounces: 4
'''
#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

print("Enter the number of ounces to convert:")
ounces = int(input())

#convert ounces to pounds and tons 
tons = ((ounces // 16) // 2000)
pounds = ((ounces // 16) % 2000)
ounces = pounds // 16

#output number of tons, remaining pounds, and remaining ounces
print(f'Tons: {tons}')
print(f'Pounds: {pounds}')
print(f'Ounces: {ounces}')