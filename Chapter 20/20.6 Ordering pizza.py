'''
A local pizza shop is selling a large pizza for $14.99. Given the number of pizzas to order as input, output the subtotal for the pizzas, and then output the total after applying a sales tax of 8%.

Output each floating-point value with two digits after the decimal point using the following statement:
print(f'Subtotal: ${your_value:.2f}')

Ex: If the input is:
    3

the output is:
    Pizzas: 3
    Subtotal: $44.97
    Total due: $48.57
'''
pizza_ordered = int(input())
pizza_cost = 14.99

sub_total = pizza_ordered * pizza_cost
tax_added = sub_total + (sub_total * 0.08)

print(f'Pizzas: {pizza_ordered}')
print(f'Subtotal: ${sub_total:.2f}')
print(f'Total due: ${tax_added:.2f}')
