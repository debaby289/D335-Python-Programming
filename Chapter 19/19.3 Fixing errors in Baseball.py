'''
The program contains syntax and logic errors. Fix the syntax errors in the Develop mode until the program executes. Then fix the logic errors.

Error messages are often long and technical. Do not expect the messages to make much sense when starting to learn a programming language. Use the messages as hints to locate the portion of the program that causes an error.

One error often causes additional errors further along in the program. For this exercise, fix the first error reported. Then try to run the program again. Repeat until all the syntax errors have been corrected.

Ex: the If input is:
    2
    3
    4
the output is:
    Last night the Dodgers scored 2
    The Yankees scored 3
    The Cubs scored 4

The total number of runs scored was 9
'''
dodgers_score = int(input())
yankees_score = int(input())
cubs_score = int(input())
total = dodgers_score + yankees_score + cubs_score

print(f"Last night the Dodgers scored {dodgers_score}")
print(f"The Yankees scored {yankees_score}")
print(f"The Cubs scored {cubs_score}")

print()

print(f"The total number of runs scored was {total}")