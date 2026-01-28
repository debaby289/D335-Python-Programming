'''
Docstring for Chapter 5.Challenges.5.11.1 Indentation Fix the program
Retype the below code. Fix the indentation as necessary to make the program work.
    if 'New York' in temperatures:
        if temperatures['New York'] > 90:
        print('The city is melting!')
        else:
            print(f"The temperature in New York is {temperatures['New York']}.")
else:
        print('The temperature in New York is unknown.')

Ex: If the input is 105, then the output is:
The city is melting!
Ex: If 'New York' is removed from the dictionary, then the output is:

The temperature in New York is unknown.
'''
temperatures = {
    'Seattle': 56.5,
    'New York': float(input()),
    'Kansas City': 81.9,
    'Los Angeles': 76.5
}

if 'New York' in temperatures:
    if temperatures['New York'] > 90:
        print('The city is melting!')
    else:
        print(f"The temperature in New York is {temperatures['New York']}.")
else:
        print('The temperature in New York is unknown.')