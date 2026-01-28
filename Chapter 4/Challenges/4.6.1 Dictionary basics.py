'''
Challenge : Dictionary basics
Level 1
Three integer and string pairs are read from input, each pair representing an authentication code sent to an email address. Complete the following steps:
    Create an empty dictionary named code_email_pairs.
    Add the following three key-value pairs to the dictionary named code_email_pairs:
        Key verification_code1 with the value email1
        Key verification_code2 with the value email2
        Key verification_code3 with the value email3
'''
verification_code1 = int(input())
email1 = input()
verification_code2 = int(input())
email2 = input()
verification_code3 = int(input())
email3 = input()

code_email_pairs = {
    verification_code1: email1,
    verification_code2: email2,
    verification_code3: email3
}

print(f'{verification_code1}: {code_email_pairs[verification_code1]}')
print(f'{verification_code2}: {code_email_pairs[verification_code2]}')
print(f'{verification_code3}: {code_email_pairs[verification_code3]}')

'''
Level 2
Dictionary room_guest_pairs contains two key-value pairs, each representing a hotel room number and the guest's name. An integer is read from input into variable key_name, representing a hotel room number in room_guest_pairs. Complete the following steps:
    Output the guest name corresponding to key_name in dictionary room_guest_pairs.
    Delete the key-value pair associated with key_name from room_guest_pairs.
'''
room_guest_pairs = {798: 'Ani', 681: 'Gus'}
key_name = int(input())

print(room_guest_pairs[key_name])
del room_guest_pairs[key_name]

print('Remaining pairs:')
print(room_guest_pairs)

'''
Level 3
Dictionary test_scores contains four key-value pairs each representing a student's name and score on a test. Complete the following steps:

Read a string from input into variable key_name, representing a student's name.
Modify the test score associated with key_name so that the updated value is the original value minus 3.
'''
test_scores = {'Mel': 42, 'Guy': 48, 'Kim': 46, 'Ava': 15}
print('Original:')
print(test_scores)

key_name = input()
test_scores[key_name] -= 3

print('Updated:')
print(test_scores)

'''
Level 4
Dictionary word_to_num contains ten key-value pairs. Complete the following steps:
    Read strings wordA and wordB from input, which together spell out a two-digit number.
    Use word_to_num to output the sum of key wordA's value and key wordB's value, which is equal to the two-digit number.
'''
word_to_num = {
	'sixty': 60, 'one': 1, 'two': 2, 'three': 3,
	'four': 4, 'five': 5, 'six': 6, 'seven': 7,
	'eight': 8, 'nine': 9
}

wordA = input()
wordB = input()

print(word_to_num[wordA] + word_to_num[wordB])
