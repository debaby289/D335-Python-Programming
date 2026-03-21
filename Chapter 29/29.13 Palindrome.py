'''
A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

Ex: If the input is:
    bob
the output is:
    palindrome: bob

Ex: If the input is:
    bobby
the output is:
    not a palindrome: bobby

Hint: Start by removing spaces. Then check if the string equals itself in reverse
'''
def palindrome(words):
    words = words.replace(' ','')

    if words == "".join(reversed(words)):
        return True
    else:
        return False

if __name__ == '__main__':
    user_input = input()

    result = palindrome(user_input)

    if result == True:
        print(f'palindrome: {user_input}')
    else:
        print(f'not a palindrome: {user_input}')
