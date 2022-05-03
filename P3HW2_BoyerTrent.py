# CTI-110
# P3HW2- pizza order
# Trent Boyer
# 30apr22


# get the number of students



print("How many students do you want to order pizza for?")

num1= int(input())

# x is the number of people sharing pizza

listA = [1.5, 2, 3]

print("Enter number of people per pizza (1.5, 2 or 3):")

num2= int(input())

total_pizzas = num1 * num2

# this is the only way I could get this to work

if num2 in listA:

# display results
    print("----Pizza Order-------")
    
    print("number of Students:", num1)
    
    print("Pizzas Needed:", total_pizzas)
    
    print("Price:$", total_pizzas * 6.00)
    
else:

    print("INVALID ENTRY!!")
    
    print("Should have entered 1.5, 2 or 3")
    
    print("\nRun Program again")
    










