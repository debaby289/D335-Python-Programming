'''
Create a program that:
    Reads a CSV file called products.csv with format:
        name,price,quantity
        Apple,1.50,100
        Banana,0.75,150
        Orange,2.00,80

Calculates total inventory value (price * quantity for all products)
Finds the most expensive product
Prints results

Expected output:
    Total inventory value: $455.00
    Most expensive product: Orange ($2.00)
'''
import csv

total_inventory_value = 0
max_price = 0
max_product = ''

with open('products.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    first_row = True
    for row in reader:
        # Skip header
        if first_row:
            first_row = False
            continue
        
        # Extract data from row
        name = row[0]
        price = float(row[1])  # Convert string to float
        quantity = int(row[2])  # Convert string to int
        
        # Calculate product value
        product_value = price * quantity
        
        # Add to total
        total_inventory_value += product_value
        
        # Check if most expensive
        if price > max_price:
            max_price = price 
            max_product = name 

# Print results
print(f'Total inventory value: ${total_inventory_value:.2f}')
print(f'Most expensive product: {max_product} (${max_price:.2f})')