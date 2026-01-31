'''
Challenge : Getting both index and value when looping: enumerate()
Level 1
List orders_queue contains three beverage names read from input. Complete the for loop using the enumerate() function to output each beverage order's position in the queue followed by the beverage's name.

Click here for example
Ex: If the input is:
coffee
juice
chai

then the output is:
#1: coffee
#2: juice
#3: chai
'''
orders_queue = [input(), input(), input()]

for (indx, beverage) in enumerate(orders_queue):
    print(f'#{indx + 1}: {beverage}')

'''
Level 2
Integer num_shoppers is read from input, representing the number of shopper names to be read from input. List shoppers_line contains the shopper names read from the remaining input. For each element in shoppers_line, output:
    'Shopper '
    the element
    ' is number '
    the element's index in the list plus one

Ex: If the input is:
4
Jen
Ada
Gil
Ben

then the output is:
Shopper Jen is number 1
Shopper Ada is number 2
Shopper Gil is number 3
Shopper Ben is number 4
'''
num_shoppers = int(input())

shoppers_line = []
for i in range(num_shoppers):
    shoppers_line.append(input())
for (indx,shopper) in enumerate(shoppers_line):
    print(f'Shopper {shopper} is number {indx + 1}')


'''
Level 3
Integer num_input is read from input, representing the number of customer names to be read from input. List customers_list contains the customer names read from the remaining input. For each element in customers_list:
    If the element's index is even, output the element followed by ' is scheduled for Thursday'.
    Otherwise, output the element followed by ' is scheduled for Monday'.

Ex: If the input is:
3
Tia
Ina
Ben

then the output is:
Tia is scheduled for Thursday
Ina is scheduled for Monday
Ben is scheduled for Thursday
Note: x % 2 == 0 returns True if x is even.
'''
num_input = int(input())

customers_list = []
for i in range(num_input):
    customers_list.append(input())
for (indx,customer) in enumerate(customers_list):
    if indx % 2 == 0:
        date = 'Thursday'
    else:
        date = 'Monday'
    print(f'{customer} is scheduled for {date}')
