
#------------------------------------------------------------
# Exercise 1: Student Name Tag
# During orientation, each student receives a printed name tag.
#
# Write a function print_name_tag(name, class_name) that prints:
# Welcome 
# Class: 
#
# Example function call:
# print_name_tag("Alicia", "3E1")
#
# Sample output:
# Welcome Alicia
# Class: 3E1


# def print_name_tag(name,class_name):
#     return f"Welcome {name}\n Class: {class_name}" 
# result = print_name_tag("Alicia", "3E1")
# print(result)








#------------------------------------------------------------
# Exercise 4: Canteen Meal Cost
# A school canteen sells rice bowls for a fixed price each.
#
# Write a function meal_cost(price, quantity) that returns
# the total cost.
#
# Then call the function and print the returned value.
#
# Example function call:
# total = meal_cost(3.5, 2)
# print("Total Cost: $", total)
#
# Sample output:
# Total Cost: $ 7.0
# def meal_cost(price,quantity):
#     total = price*quantity
#     return f"total cost is ${total}"
# result = meal_cost(3.5,2)
# print(result)





# Exercise 9: Concert Ticket Booking
# A school concert sells:
# - student tickets at $6 each
# - adult tickets at $12 each
#
# Write a function get_ticket_price(ticket_type, quantity)
# that returns the total ticket price.
def get_ticket_price(ticket_type, quantity):
    if ticket_type == "student":
        total = 6*quantity
    else:
        total = 12*quantity
    return f"total ticket price is {total}"
# Then write a function booking_summary(name, ticket_type, quantity)
# that calls get_ticket_price() and prints:
# Name: 
# Ticket Type: 
# Quantity: 
# Total Price: $
def booking_summary(name, ticket_type, quantity):
    return f"name: {name}\nTicket type: {ticket_type}\nQuantity: {quantity}\nTotal Price: {get_ticket_price(ticket_type,quantity)}"
# Example function call:
# booking_summary("Rina", "student", 4)
#
# Sample output:
# Name: Rina
# Ticket Type: student
# Quantity: 4
# Total Price: $24
result = booking_summary("randall", "student", 4)
print(result)
