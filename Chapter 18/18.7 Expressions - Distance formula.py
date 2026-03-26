'''
Docstring for Chapter 18.Easy.18.7 Expressions - Distance formula
Map/GPS applications commonly compute the distance between two points. A point may be a coordinate on an x-y plane like (1.5, 2.0). The distance formula is d = √((x2 - x1)2 + (y2 - y1)2) (basically, Pythagorean's Theorem). Given two points, output the distance between the two points. Round the distance to 2 decimal places.

If the input is:
1.5
2.0
4.5
6.0
representing (1.5, 2.0) and (4.5, 6.0), the output is
5.0
Hints: Use the math module.

Note: Read the input values as float and end the output with a newline.
'''
import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

d = math.sqrt((math.pow((x2 - x1),2)) + (math.pow((y2 - y1),2)))

'''
d = √((x2 - x1)^2 + (y2 - y1)^2) 
squart root of ((x2 - x1)^2 + (y2 - y1)^2) = math.sqrt((math.pow((x2 - x1),2)) + (math.pow((y2 - y1),2)))
(x2 - x1)^2 = math.pow((x2 - x1),2)
(y2 - y1)^2 = math.pow((y2 - y1),2)
'''
print(round(d,2))
#print(f'{d:.2f}')