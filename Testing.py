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
