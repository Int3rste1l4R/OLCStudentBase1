
# Exercise 7: Greeting Multiple Users
# Write a function that takes a list of names and greets each one.


# Call the function with a list of names.
# greet_users(["Alice", "Bob", "Charlie"])
# names = ["Alice", "Bob", "Charlie"]

# def greeting(list_names):
#     for name in list_names:
#         print(f"hello {name}")
        
# greeting(names)

list_nums = [25,56,47,56,34,36,8,78,554,345,456]
# write a function to calculate the cube of a number
total = 0
def cube_num(num):
    cube = num**3
    return cube
    
for num in list_nums:
    number = cube_num(num)
    total = total + number
print(total)

# call the function to calculate the sum of all the cubes... 



#------------------------------------------------------------
# Exercise 9: Palindrome Checker
# Write a function that checks if a string is a palindrome.
# word_check = str(input("enter word: "))
# def palidrome_check(word):
#     if word[::-1] == word:
#         # print("palindrome")
#         return True
#     else:
#         # print("not palindrome")
#         return False
#     # return word
# print(palidrome_check(word_check))

# Test the function with different words.
# print("Is 'radar' a palindrome? {}".format(is_palindrome("radar")))
# print("Is 'hello' a palindrome? {}".format(is_palindrome("hello")))







#------------------------------------------------------------
# Exercise 10: Display Multiplication Table
# Write a function that takes a number and prints its multiplication table.
# def multiplication_table(num): 

#     # multiplier = 1
   
#     for i in range(1, 13):
#         print(f"{num} x {i} = {num*i}")
#         # multiplier += 1

# num = int(input("enter number: "))
# multiplication_table(num)


###########################################################
# Part 2. IN-CLASS Practice Exercises
# Topic: Creating Functions and Calling Functions


# =========================================================
# A. FUNCTIONS THAT PRINT RESULTS DIRECTLY
# (The function itself prints the output.)
# =========================================================

#------------------------------------------------------------
# Exercise 1: Student Name Tag
# During orientation, each student receives a printed name tag.
#
# Write a function print_name_tag(name, class_name) that prints:
# Welcome 
# Class: 
# def print_name_tag(name, class_name):
#     print(f"welcome {name} \nclass: {class_name}")

# print_name_tag("alicia","3E1")
# print(print_name_tag(name, class_name))
# Example function call:
# print_name_tag("Alicia", "3E1")
#
# Sample output:
# Welcome Alicia
# Class: 3E1





#------------------------------------------------------------



#------------------------------------------------------------
# Exercise 2: Hotel Booking Charge
# A hotel charges $120 per night for a room.
#
# Write a function booking_confirmation(guest_name, nights) that
# calculates the total cost and prints:
# Booking confirmed for 
# Number of nights: 
# Total cost: $
# def booking_confirmation(guest_name, nights):
#     total_cost = nights*120
#     print(f"booking confirmed for {guest_name} \nnumber of nights: {nights} \ntotal cost: ${total_cost}")
# booking_confirmation("Mr Lee",3)
# # Example function call:
# booking_confirmation("Mr Lee", 3)
#
# Sample output:
# Booking confirmed for Mr Lee
# Number of nights: 3
# Total cost: $360



#------------------------------------------------------------
# Exercise 4: Canteen Meal Cost
# A school canteen sells rice bowls for a fixed price each.
#
# Write a function meal_cost(price, quantity) that returns
# the total cost.
# def meal_cost(price, quantity):
#     total = price*quantity #price(cost,number)### 
#     return total

# inp_cost = float(input("enter cost of food: "))
# inp_number = int(input("enter amount of food: "))
# total_cost = meal_cost(inp_cost,inp_number)
# print(total_cost)
# Then call the function and print the returned value.
#
# Example function call:
# total = meal_cost(3.5, 2)
# print("Total Cost: $", total)
#
# Sample output:
# Total Cost: $ 7.0


# The following program has a dictionary that contains drink flavours and their prices. 
# The program allows the user to:

# calculate the total price of drinks ordered based on the flavour and amount of cups
# add or remove flavour-price pairs
# The task is to edit the program code so that

# allows user to input whether they want to calculate the price of an order
# the total price of an order can be output based on a dictionary
# allows user to input whether they want to add or remove a flavour and its price in the dictionary
# keeps running until the user inputs the desire to exit the program.

def admin_mode():
    print()

def cashier_mode():
    print()
# main

# pricing
price_flavour = {
    "coffee": 5.50,
    "vanilla": 4.50,
    "caramel": 6.50,
    "hazelnut": 4.00
}

# cashier interface
# mode = input("Select mode (A/C/E): ")
    
# For each of the sub-tasks, add a comment using the hash symbol # 
# at the beginning of your code to indicate the sub-task 
# that the program code belongs to. For example:





 
#___________________________________________________________
# Task 2.2
# Copy and paste your program from sub-task 2.1.

# Edit the function cashier_mode(), that has no parameters, so that it:

# allows the user to input the flavour of a drink
# allows the user to input the number of cups for that flavour
# uses the dictionary price_flavour and outputs the total price for the order.
# [3]
#___________________________________________________________


price_flavour = {
    "coffee": 5.50,
    "vanilla": 4.50,
    "caramel": 6.50,
    "hazelnut": 4.00
}

def cashier_mode(flavour,quantity):

    cost = price_flavour[flavour]
    total_cost = cost*quantity
    return total_cost

flavour = str(input("what flavour? "))
amount = int(input("how many cups? "))

total = cashier_mode(flavour,amount)
print(f"${total} for {amount} cups of {flavour}")


# Task 5.4 [6]
# Create a simple text-based user interface that:
# •	Prompts and validates today’s date in "DD-MM" format.
# o	You must use the validate_date() function to validate today’s date. 
# Your program will keep asking for an input until a valid date is provided.

# •	Prompts and validates the expiry date in "DD-MM" format.
# o	You must use the validate_date() function to validate the expiry date. 
# Your program will keep asking for an input until a valid date is provided.

# •	Compute if the item has expired. You must use the days_difference() function. 
#     If the number of days is positive, the item has not expired. 
#          Output “Item is fresh and will expire in  days.”
#     If the number of days is negative, the item has expired. 
#          Output “Item has expired  days ago.”
#     If the number of days is 0, then the item expires today. 
        #    Output “Item will expire today!”
# ________________________________________