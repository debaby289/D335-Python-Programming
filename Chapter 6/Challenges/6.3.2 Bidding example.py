'''
Docstring for Chapter 6.Challenges.6.3.2 Bidding example
Variable keep_bidding is initially assigned with 'y'. Within the while loop, keep_bidding is updated with the user's next input value. Complete the while loop's expression to terminate the while loop if the user enters 'n'.

Ex: If the input is 'y' 'y' 'n', then the output is:
I'll bid $10!
Continue bidding? (y/n) I'll bid $15!
Continue bidding? (y/n) I'll bid $21!
Continue bidding? (y/n)
'''
import random
random.seed(5)

keep_bidding = 'y'
next_bid = 0

while keep_bidding == 'y':
   next_bid = next_bid + random.randint(1, 10)
   print(f'I\'ll bid ${next_bid}!')
   print('Continue bidding? (y/n)', end=' ')
   keep_bidding = input()