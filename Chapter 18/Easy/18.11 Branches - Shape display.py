'''
Docstring for Chapter 18.Easy.18.11 Branches - Shape display
A user inputs the name of a shape (square or triangle). The program outputs the shape using asterisks. For input "square", the output is:
***
* *
***
If the input is "triangle", the output is:

  *
 * *
*****
'''
shape = input()

if shape == "square":
    print("***")
    print("* *")
    print("***")
elif shape == "triangle":
    print("  *")
    print(" * *")
    print("*****")