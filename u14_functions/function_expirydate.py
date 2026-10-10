##############################################################
##### MOCK QUESTION ##########################################
##############################################################
# The task is to write a program that checks whether a food item has expired based on 
# its expiry date and today’s date. Dates are entered in the format "DD-MM".

# All code should have appropriate comments and meaningful identifiers. [2]
# 
# ________________________________________
# Task 5.1 [4]
# Write a calculate_days( ) function that accepts a date parameter in the format "DD-MM".
# The function must calculate and return the total number of days elapsed since 01-01, 
# assuming 30 days per month
# ________________________________________
def calculate_days(date):
    day = int(date[:2])
    month = int(date[3:])
    elapse = (month - 1)*30 + day
    return elapse















# Test your code using the values below
# print(calculate_days("01-02"))
# print(calculate_days("30-01"))
# print(calculate_days("30-02"))
# print(calculate_days("30-12"))


# ________________________________________
# Task 5.2  [3]
# Write a days_difference( ) function that takes two parameters:
# •	today (format "DD-MM")
# •	expiry (format "DD-MM")

# The function will check if an item has expired and return the number of days 
# between today’s date and the expiry date.
# •	Expiry is calculated by subtracting the today’s date from the expiry date. 
# You must use the calculate_days() function to retrieve the number of days between 
# today’s date and expiry date. Note that the number of days could be negative.
# You can assume both dates are always within the same year.
# 
# ________________________________________
def days_difference(today, expiry):
    today_diff = calculate_days(today)
    expiry_diff = calculate_days(expiry)
    total_days = expiry_diff - today_diff
    return total_days






# print(days_difference("11-07", "12-07")) # 1
# print(days_difference("11-07", "10-07")) # -1
# print(days_difference("11-07", "11-07")) # 0
# print(days_difference("01-07", "15-07")) # 15



# ________________________________________
# Task 5.3 [8]
# Write a validate_date( ) function that accepts one parameter:
# •	date_str (a string in the format "DD-MM")
# The function must check whether the input date is valid according to the following rules:
# 1.	The input must contain a dash (-) separator between day and month.
# 2.	Both the day (DD) and month (MM) must be two characters long (e.g. "05-04" not "5-4").
# 3.	The day (DD) must be between 1 and 30 (inclusive).
# 4.	The month (MM) must be between 1 and 12 (inclusive).
# If all conditions are met, the function should return True.
# If any condition fails, the function should return False.
# Displays appropriate messages for invalid input. You may assume the input is always a string.
# ________________________________________

def validate_date(date_str):
    if len(date_str) != 5:
        print("Date Length must be 5 characters long.")
        return False
    elif date_str[2] != "-":
        print(" date must have a '-' in the middle")
        return False
    elif not date_str[:2].isdigit() or not date_str[3:].isdigit():
        print(" date is not a number")
        return False
    elif int(date_str[:2]) < 1 or int(date_str[:2]) > 30:
        print("date is not between 1 and 30")
        return False
    elif int(date_str[3:]) > 12 or int(date_str[3:]) < 1:
        print("month is not between 1 and 12")
        return False
    else:
        print("valid date")
        return True
    














# print(validate_date("35-01"))
# print(validate_date("aa-01")) 
# print(validate_date("01-aa")) 
# print(validate_date("50-01"))
# print(validate_date("05-50"))
# print(validate_date("03-10"))

# ________________________________________
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
while True:
    today_date = input("enter today's date in DD-MM: ")
    if validate_date(today_date) == False:
        print("invalid date")
    else:
        print("valid date")
        break
while True:
    expire_date = input("enter expiry date in DD-MM: ")
    if validate_date(expire_date) == False:
        print("invalid date")
    else:
        print("valid date")
        break
difference = days_difference(today_date, expire_date)
if difference > 1:
    print(f"{difference} days until it expires")
elif difference < 1:
    print(f"it expired { abs(difference)} days ago")
else:
    print("it expires today")