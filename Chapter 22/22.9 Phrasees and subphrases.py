'''
Write a program that reads two phrases on separate lines and outputs one of four responses:

1) Phrase one is found within phrase two
2) Phrase two is found within phrase one
3) Both phrases match
4) No matches

Hint: Use membership operator in.

Ex: If the input is:
    fire
    firetruck
the output is:
    fire is found within firetruck

Ex: If the input is:
    the green grass grows
    green grass
the output is:
    green grass is found within the green grass grows

Ex: If the input is:
    pick a card
    pick a card
the output is:
    Both phrases match

Ex: If the input is:
    apples
    oranges
the output is:
    No matches
'''
phrase_one = input()
phrase_two = input()

if phrase_one == phrase_two:
    print('Both phrases match')
elif phrase_one in phrase_two:
    print(f'{phrase_one} is found within {phrase_two}')
elif phrase_two in phrase_one:
    print(f'{phrase_two} is found within {phrase_one}')
else:
    print('No matches')