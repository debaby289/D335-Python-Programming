'''
Docstring for Chapter 6.Challenges.6.3.3 While loop Insect growth
Positive integer num_insects is read from input. Write a while loop that in each iteration first prints and then doubles num_insects. The loop executes while values are less than or equal to 100. Output each number on a newline.

Ex: If the input is: 8, then the output is:
8
16
32
64
'''
num_insects = int(input())

while num_insects <= 100:
    print(num_insects)
    num_insects *= 2