# ============================================================
# Movie Ticket Booking System
# Total: 25 marks
# ============================================================

"""
A cinema is creating a simple ticket booking system for one movie hall.

The movie hall has 5 rows of seats:
A, B, C, D and E

Each row has 20 seats, numbered from 01 to 20.

A valid seat code has exactly 3 characters.

Examples of valid seat codes:
A01
A12
B05
E20

Examples of invalid seat codes:
F01     # invalid row
A00     # invalid seat number
C21     # invalid seat number
A1      # invalid format
AA1     # invalid format
B05X    # invalid length

Each movie ticket costs $12.

The cinema staff will enter bookings for different customers.

For each customer, the program should:
1. Ask for the customer's name.
2. Ask for the number of tickets the customer wants to book.
3. Ask for and validate the seat code for each ticket.
4. Store the customer's booking.
5. Display all current customer bookings.

Keep asking until the user wants to stop entering more names

After the user stops,  the program should display a daily summary showing:
1. Each customer's name.
2. The amount paid by each customer.
3. The total payment received for the day.

You are not required to use functions for this question.
"""
overall_booked_seats = ["A01","A02","A03"] # list containing all seats booked across all customers
customer_booked_seats = [] # list to store specific customer seats
current_bookings = {"ALI":["A01","A02","A03"]} # dictionary containing all customers and their bookings

# ============================================================
# Task 1: Ask for customer names repeatedly
# [3 marks]
# ============================================================

"""
Write Python code to repeatedly ask the user to enter a customer's name.

- The customer name must not be blank.
- The customer name should be stored in uppercase.

If the user enters a blank name, display a suitable error message and ask
for the customer name again.

After a valid customer name is entered, the program should continue to
Task 2 for that customer.
"""

# Write your code for Task 1 below
# while True:
#     customer_name = input("what is your name? ")
#     if customer_name == "":
#         print("please input a valid name")
#     else:
#         customer_name = customer_name.upper()
#         break
# print(customer_name)






# ============================================================
# Task 2: Ask for the number of tickets
# [3 marks]
# ============================================================

"""
For each customer, ask for the number of tickets the customer wants to book.

- The number of tickets must be a whole number from 1 to 5 inclusive.
- If the input is invalid, display a suitable error message and ask again.
- The program should only continue to Task 3 after a valid number of tickets
  has been entered.
"""
# Copy and paste your code from previous task



while True:
    customer_name = input("what is your name? ")
    if customer_name == "":
        print("please input a valid name")
    else:
        customer_name = customer_name.upper()
        break
print(customer_name)
# Write your code for Task 2 below
while True:
    ticket_no = input("Enter number of tickets bought: ")
    if ticket_no.isdigit() == False:
        print("invalid")
    elif int(ticket_no) <1 or int(ticket_no) >5:
        print("invalid")
    else:
        print("valid")
        break


# ============================================================
# Task 3: Ask for and validate seat codes
# [9 marks]
# ============================================================

"""
For each customer, ask the user to enter one valid seat code for each ticket.

For example, if the customer wants to book 3 tickets, the program should
accept exactly 3 valid seat codes for that customer.

Each seat code entered should be converted to uppercase.

A valid seat code must satisfy all of the following conditions:

1. It has exactly 3 characters.
2. The first character is one of the row letters:
   A, B, C, D or E.
3. The last two characters are digits.
4. The seat number is from 1 to 20 inclusive.
5. The seat has not already been been booked.

If the seat code is invalid, display a suitable error message and ask for
another seat code.

If the seat code is valid, store it as one of the current customer's seats.
The row must be stored in upper case

The program should only continue to Task 4 after the current customer has
successfully selected all required seats.
"""

# Write your code for Task 3 below

# This variable contains all booked seats across different customers.
overall_booked_seats = ["A01","A02","A03"]
customer_booked_seats = []





# ============================================================
# Task 4: Store and display all current bookings
# [4 marks]
# ============================================================

"""
After the current customer has selected all required seats, store the customer's
booking.

The booking should be stored so that each customer name is linked to the list
of seats booked by that customer.

After storing the current customer's booking, display all current customer
bookings.

Example output:

Current Bookings
----------------
ALI : ['A01', 'A02']
MEI : ['B10']
RAVI : ['C05', 'C06', 'C07']

After displaying the current bookings, the program should ask for the next
customer's name.

This process should continue until the user enters "END" as the customer name.
"""

# Write your code for Task 4 below





# ============================================================
# Task 5: Display the daily payment summary
# [4 marks]
# ============================================================

"""
After the user enters "END" as the customer name, display the daily payment
summary.

The summary should show:

1. Each customer's name.
2. The amount paid by each customer.
3. The total payment received for the day.

The amount paid by each customer is calculated using the number of seats
booked by that customer.

Example output:

Daily Summary
-------------
ALI paid $24
MEI paid $12
RAVI paid $36

Total payment received: $72
"""

# Write your code for Task 5 below





# ============================================================
# Quality of Program
# [2 marks]
# ============================================================

"""
Award up to 2 marks for:

1. Meaningful variable names.
2. Clear comments where appropriate.
3. Code that is neat, readable and properly indented.
"""


# ============================================================
# End of Question
# ============================================================
