'''
Write a program that compares two strings given as input. Output the number of characters that match in each string position. The output should use the correct verb (match vs matches) according to the character count.

Ex: If the input is:
    crash
    crush
the output is:
    4 characters match

Ex: If the input is:
    cat
    catnip
the output is:
    3 characters match

Ex: If the input is:
    mall
    saw
the output is:
    1 character matches

Ex: If the input is:
    apple
    orange
the output is:
    0 characters match
'''
word_one = input()
word_two = input()
count = 0

if len(word_one) > len(word_two):
    final_judgement = word_two
else:
    final_judgement = word_one

for word in range(len(final_judgement)):
    if word_one[word] == word_two[word]:
        count += 1

if count == 1:
    print(f'{count} character matches')
else:
    print(f'{count} characters match')
