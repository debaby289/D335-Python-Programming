'''
Task:
Create a solution that accepts any three integer inputs representing the base (b1, b2) and height (h) measurements of a trapezoid in meters. Output the exact area of the trapezoid in square meters as a float value. The exact area of a trapezoid can be calculated by summing the two bases, multiplying the sum by the height, and then dividing by two.

Trapezoid Area Formula:
    A = ((b1 + b2) * h) / 2

The solution output should be in the format:
    Trapezoid area: area_value square meters

Sample Input and Output:
    If the input is
    Enter base 1: 3
    Enter base 2: 4
    Enter height: 5
then the expected output is
    Trapezoid area: 17.5 square meters

Alternatively, if the input is
    Enter base 1: 3
    Enter base 2: 5
    Enter height: 7
then the expected output is
    Trapezoid area: 28.0 square meters
'''
#solution accepts three integer values representing base and height measurements of a trapezoid
#first and second integers represent base 1 and base 2; third integer represents height 
#solution outputs the trapezoid area in square meters using formula A = ((b1 + b2) * h) / 2)
print("Enter base 1: ")
base_1 = int(input())
print("Enter base 2: ")
base_2 = int(input())
print("Enter height: ")
height = int(input())

#calculate the area of a trapezoid
area = ((base_1 + base_2) * height) / 2

#ouput exact trapezoid area based on input dimensions
print(f'Trapezoid area: {area} square meters')