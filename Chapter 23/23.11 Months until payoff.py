'''
Write a program that reads a loan amount, payment amount, and interest rate as inputs and outputs the number of payments required until the loan is paid. Interest is added to current balance before a payment is applied. Ex: If current balance is $100.00 and the interest rate is 0.02, the new balance is $102.00 before a payment is applied. All values are floats.

Ex: If the input is:
    1000.0
    50.0
    0.03

the output is:
    31 payments

Ex: If the input is:
    50.0
    100.0
    0.02

the output is:
    1 payment
'''
loan = float(input())
payment = float(input())
interest = float(input())
count = 0

while loan > 0:
    loan = loan + (loan * interest)
    loan -= payment
    count += 1

if count == 1:
    print(f'{count} payment')
else:
    print(f'{count} payments')

