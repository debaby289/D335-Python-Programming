'''
Challenge : Counting using the range() function
Level 1
Positive integer glove_pairs is read from input, representing the number of glove pairs. Complete the range() function call so that the for loop iterates through the increasing sequence of all non-negative integers less than glove_pairs times 2.
'''
glove_pairs = int(input())

print('Gloves are numbered:', end=' ')

for i in range(glove_pairs * 2):
    print(i, end=' ')
print()

'''
Level 2
Positive integers seat_start and seat_stop are read from input, representing the seat numbers allocated to party guests, with seat_start less than seat_stop. Complete the for loop to iterate through the increasing sequence of all integers between seat_start and seat_stop both exclusive.
'''
seat_start = int(input())
seat_stop = int(input())

print('Seat numbers:', end=' ')

for i in range(seat_start + 1,seat_stop,1):
    print(i, end=' ')
print()

'''
Level 3
Integers ticket_hi and ticket_low are read from input, representing a range of ticket numbers issued for a museum tour. ticket_hi is greater than ticket_low. Complete the for loop as follows:
    Use ticket_val as the loop variable.
    Iterate through the decreasing sequence of all the integers from ticket_hi down to ticket_low, both inclusive.
'''
ticket_hi = int(input())
ticket_low = int(input())

print('Tickets issued:', end=' ')

for ticket_val in range(ticket_hi, ticket_low - 1, -1):
    print(ticket_val, end=' ')
print()

'''
Level 4
Integer num_dozens is read from input, representing how many dozens of oranges are purchased. For every integer between 1 and num_dozens, both inclusive, output the integer's value followed by ' dozen(s) of oranges = ', the integer's value times 12, and ' oranges'.
'''
num_dozens = int(input())
for dozen in range(num_dozens + 1):
    oranges_amount = dozen * 12
    print(f'{dozen} dozen(s) of oranges = {oranges_amount} oranges')