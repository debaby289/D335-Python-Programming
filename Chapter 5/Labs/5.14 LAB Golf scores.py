'''
Docstring for Chapter 5.Labs.5.14 LAB Golf scores

Golf scores record the number of strokes used to get the ball in the hole. The expected number of strokes varies from hole to hole and is called par (possible values: 3, 4, or 5). Each score's name is based on the actual strokes taken compared to par:
    "Eagle": number of strokes is two less than par
    "Birdie": number of strokes is one less than par
    "Par": number of strokes equals par
    "Bogey": number of strokes is one more than par

Given two integers that represent the number of strokes used and par, write a program that prints the appropriate score name. Print "Error" at the end of the output if par is not 3, 4, or 5, or if the score's name is not "Eagle", "Birdie", "Par", or "Bogey".

Ex: If the input is:
3
4

the output is:
Par 4 in 3 strokes is Birdie
'''
stroke = int(input())
par = int(input())

score_keep = par - stroke

if par not in (3, 4, 5):
    print(f'Par {par} in {stroke} strokes is Error')
elif score_keep == 2:
    print(f'Par {par} in {stroke} strokes is Eagle')
elif score_keep == 1:
    print(f'Par {par} in {stroke} strokes is Birdie')
elif score_keep == 0:
    print(f'Par {par} in {stroke} strokes is Par')
elif score_keep == -1:
    print(f'Par {par} in {stroke} strokes is Bogey')
else:
    print(f'Par {par} in {stroke} strokes is Error')