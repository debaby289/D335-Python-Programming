'''
Challenge : String slicing
Level 1
Integers start_index and end_index are read from input. Assign partial_quote with the result of slicing orig_quote from start_index to end_index.

Click here to show example
Ex: If the input is:
4
6

then the output is:
Full quote: The only true wisdom is in knowing you know nothing
Sliced quote: on
'''
start_index = int(input())
end_index = int(input())
orig_quote = 'The only true wisdom is in knowing you know nothing'

partial_quote = orig_quote[start_index:end_index]

print('Full quote:', orig_quote)
print('Sliced quote:', partial_quote)

'''
Level 2
String saying is read from input. Assign variable sliced_string with the last three characters of saying.

Click here to show example
Ex: If the input is:
To be or not to be, that is the question

then the output is:
ion
'''
saying = input()

sliced_string = saying[-3]

print(sliced_string)

'''
Level 3
String orig_string is read from input. Assign variable sliced_string with the orig_string slice that excludes the character at index 13.

Click here to show example
Ex: If the input is:
The only limit to our realization of tomorrow will be our doubts

then the output is:
The only limi to our realization of tomorrow will be our doubts
'''
orig_string = input()

sliced_string = orig_string[0:13] + orig_string[14:]

print(sliced_string)

'''
Level 4
Integer stride_len is read from input. Assign variable partial_string with every stride_len element of full_string's last half.

Ex: If the input is 2, then the output is:
Full string: elderberry
Sliced string: bry
'''
stride_len = int(input())
full_string = 'elderberry'

starting_index = (len(full_string)) // 2
partial_string = full_string[starting_index::stride_len]

print('Full string:', full_string)
print('Sliced string:', partial_string)