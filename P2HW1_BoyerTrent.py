# Total purchases calc
# 15apr22
# CTI-110 P2HW1 - Total Purchases
# trenton boyer

# 
sales_tax = .07

# 5 user inputs "float" for fractional numbers

item1 = float(input('\nEnter the price of item #1: $'))
item2 = float(input('Enter the price of item #2: $'))
item3 = float(input('Enter the price of item #3: $'))
item4 = float(input('Enter the price of item #4: $'))
item5 = float(input('Enter the price of item #5: $'))

# add the inputs for a subtotal
subtotal =  float(item1) + float(item2) + float(item3) +\
                  float(item4) + float(item5)
# find sales tax after subtotal
total_sales_tax = subtotal * sales_tax
# calculate overall total
total = subtotal + total_sales_tax
# print requirements
print("-------Results_______")
print('Subtotal:',subtotal)
print('Sales Tax:', total_sales_tax)
print('Total:', total)
