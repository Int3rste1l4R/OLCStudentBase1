# A school tuck shop wants a digital system to track stock levels 
# of items it sells. You are required to build a module that lets 
# a staff member enter item names and their stock quantities into 
# a centralized system.

# The program must ensure all entered quantities are non-negative 
# whole numbers. Once the staff member has finished entering all 
# data, the program should automatically generate a stock summary: 
# the total number of distinct items, the item(s) with the highest 
# stock quantity, and the total number of items in stock overall.

#=================================================
# Task 1
# Write a program that uses a while loop to collect stock data.
# The program must prompt for an Item Name and then a Quantity.
# The loop should terminate only when the word "done" is 
# entered for the Item Name. [2]
#=================================================
# while True:
#     Item_name = input("enter item name: ")
#     if Item_name == "done":
#         break
#     else:
#         Quantity = input("enter quantity: ")


#=================================================
# Task 2
# Copy and paste your program from Task 1.
# Add validation checks:
# - ensure the item name is not just whitespace.
# - ensure the quantity contains only numbers.
# - ensure the quantity is not negative.
# If the quantity is invalid, display an error message and 
# prompt the user to re-enter the quantity for that specific item. [4]
#=================================================
# while True:
#     while True:
#         Item_name = input("enter item name: ")

#         if Item_name == "":
#             print("invalid name.")
#         else:
#             break
#     if Item_name == "done":
#             break
#     while True:
#         Quantity = input("enter quantity: ")
#         if not Quantity.isdigit():
#             print("invalid quantity.")
#         elif int(Quantity) < 0:
#             print("quantity cannot be less than 0.")
#         else:
#             break
        



#=================================================
# Task 3
# Copy and paste your program from Task 2.
# Store the validated item name and quantity in a dictionary named 
# stock_book. If the same item name is entered again, UPDATE its 
# quantity (add the new amount to the existing one) instead of 
# creating a duplicate entry.
# Once the loop ends, use the dictionary to display:
# - The total number of distinct items recorded.
# - The item name(s) with the highest stock quantity (there may 
#   be more than one item tied for highest — display all of them).
# - The total number of items in stock overall (sum of all quantities). [5]
#=================================================
stock_book = {}
highest = 0
highest_items = []
total = 0
while True:
    while True:
        Item_name = input("enter item name: ")

        if Item_name == "":
            print("invalid name.")
        else:
            break
    if Item_name == "done":
            break
    while True:
        Quantity = input("enter quantity: ")
        if not Quantity.isdigit():
            print("invalid quantity.")
        elif int(Quantity) < 0:
            print("quantity cannot be less than 0.")
        else:
            stock_book[Item_name] = int(Quantity)
            break
print(f"the total number of items is {len(stock_book)}.")
for key,value in stock_book.items():
    if value > highest:
        highest = value
        highest_items = [key]
    elif value == highest:
        highest_items.append(key)
    total = total + value
print(f"{highest_items} has the highest quantity of {highest} ")
print(f"the total number of items in stock is {total}")