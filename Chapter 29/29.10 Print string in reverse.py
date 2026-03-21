'''
Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:
    Hello there
    Hey
    done

then the output is:
    ereht olleH
    yeH
'''
phrases = [input()]

#Track inputs
while ('Done','done','d') not in phrases:
    second_input = input()
    if second_input in ('Done','done','d'):
        break
    else:
        phrases.append(second_input)

#Split phrases
for phrase in phrases:
    for i in range(len(phrase)-1,-1,-1):
        print(f'{phrase[i]}',end='')
    print()