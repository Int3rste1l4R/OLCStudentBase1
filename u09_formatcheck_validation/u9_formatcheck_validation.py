# ###################################################
# # Part 1: Learning Exercises

# # Exercise 1: Converting to Uppercase
# # Write a program to convert a string to uppercase.
# # Example: Input = "hello", Output = "HELLO".
# word = "hello"
# uppercase_word = word.upper()  # Convert to uppercase
# print("Uppercase: {}".format(uppercase_word))




# #------------------------------------------------------------
# # Exercise 2: Converting to Lowercase
# # Write a program to convert a string to lowercase.
# # Example: Input = "HELLO", Output = "hello".
# word = "HELLO"
# lowercase_word = word.lower()  # Convert to lowercase
# print("Lowercase: {}".format(lowercase_word))




# #------------------------------------------------------------
# # Exercise 3: Checking if a String is Uppercase
# # Write a program to check if a string is fully uppercase.
# # Example: Input = "HELLO", Output = True.
# word = "HELLO"
# is_upper = word.isupper()  # Check if uppercase
# print("Is '{}' uppercase? {}".format(word, is_upper))




# #------------------------------------------------------------
# # Exercise 4: Checking if a String is Lowercase
# # Write a program to check if a string is fully lowercase.
# # Example: Input = "hello", Output = True.
# word = "hello"
# is_lower = word.islower()  # Check if lowercase
# print("Is '{}' lowercase? {}".format(word, is_lower))




# #------------------------------------------------------------
# # Exercise 5: Checking if a String is Alphanumeric
# # Write a program to check if a string contains only letters 
# # and numbers.
# # Example: Input = "Python123", Output = True.
# word = "Python123"
# is_alnum = word.isalnum()  # Check if alphanumeric
# print("Is '{}' alphanumeric? {}".format(word, is_alnum))




# #------------------------------------------------------------
# # Exercise 6: Checking if a String is Alphabetic
# # Write a program to check if a string contains only letters.
# # Example: Input = "Python", Output = True.
# word = "Python"
# is_alpha = word.isalpha()  # Check if alphabetic
# print("Is '{}' alphabetic? {}".format(word, is_alpha))




# #------------------------------------------------------------
# # Exercise 7: Checking if a String is Numeric
# # Write a program to check if a string contains only numbers.
# # Example: Input = "12345", Output = True.
# word = "12345"
# is_digit = word.isdigit()  # Check if numeric
# print("Is '{}' numeric? {}".format(word, is_digit))




# #------------------------------------------------------------
# # Exercise 8: Removing Extra Spaces
# # Write a program to remove leading and trailing spaces.
# # Example: Input = "  hello  ", Output = "hello".
# word = "  hello  "
# stripped_word = word.strip()  # Remove spaces
# print("Stripped string: '{}'".format(stripped_word))




# #------------------------------------------------------------
# # Exercise 9: Length Validation
# # Write a program to validate that a string has at least 5 
# # characters. Prompt the user repeatedly until they enter a 
# # valid string.
# while True:
#     user_input = input("Enter a string with at least 5 characters: ")
#     if len(user_input) >= 5:
#         break  # Exit loop if valid
#     print("String too short. Try again.")
# print("Valid string: {}".format(user_input))




#------------------------------------------------------------
###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 10: Validating Uppercase Input
# Scenario: You are entering product codes into a system, and 
# all codes must be in uppercase letters (e.g., "ABC123").
# while True:
#     code = input("enter code: ")
#     if code.isupper():
#         print("code valid")
#         break
#     else:
#         print("code invalid")








#------------------------------------------------------------
# Exercise 11: Validating Alphanumeric Input
# Scenario: A username field only accepts alphanumeric characters
# (letters and numbers) without special symbols
# while True:
#     user = input("enter user: ")
#     if user.isalnum():
#         print("valid user")
#         break
#     else:
#         print("invalid user")





#------------------------------------------------------------
# Exercise 12: Validating Numeric Input
# Scenario: You are collecting a phone number that must contain 
# only numeric characters
# while True:
#     phonenum = input("enter phone number: ")
#     if phonenum.isdigit():
#         print("valid")
#         break
#     else:
#         print("invalid phonenumber")



#------------------------------------------------------------
# Exercise 13: Checking for Substrings
# Scenario: You are searching for the word "Python" in user 
# feedback to categorize responses related to Python programming.
# while True:
#     usernam = input("enter username: ")
#     if "python" in usernam:
#         print("valid user")
#         break
#     else:
#         print("invalid user")






#------------------------------------------------------------
# Exercise 14: Replacing Parts of a String
# Scenario: A user entered their old email address, and you 
# need to replace it with a new domain (e.g., from "@old.com" to "@new.com").
# email = input("enter your email: ")
# email = email.replace("@old.com","@new.com")
# print(email)


#------------------------------------------------------------



# ============================================================
# Exercise 7: Student ID
# ============================================================

'''
Ask the user to enter a student ID.

The student ID must:
- Be exactly 6 characters long
- Start with "S"
- Have 5 digits after "S"

Examples:
S00001
S12345
S99999

Keep asking until a valid input is entered.
'''
# while True:
#     StudentID = input("enter student id: ")
#     if StudentID[0] != "s":
#         print("musts start with s")
#     elif len(StudentID) != 6:
#         print("must be 6 char long")
#     elif StudentID[1:].isdigit() == False:
#         print("must have 5 num after S")
#     else:
#         print("valid StudentID")
#         break


#--------------------------------------------------------------------
# Write your code here





# ============================================================
# Exercise 1: Singapore Postal Code
# ============================================================

'''
Ask the user to enter a Singapore postal code.

The postal code must:
- Be exactly 6 digits long
- Contain digits only

Keep asking until a valid input is entered.
'''
# while True:
#     postalcode = input("enter postal code: ")
#     if len(postalcode) != 6:
#         print("must be 6 digits")
#     elif postalcode.isdigit() == False:
#         print("must all be numbers")
#     else:
#         print("valid postalcode")
#         break
#--------------------------------------------------------------------
# Write your code here


# word = "SINGAPORE"

# # SIN
# print(word[:3])

# # GAP
# print(word[3:6])

# word = "SINGAPOOOOOOORE"
# # ORE  ## always retrieve last 3 characters
# print(word[-3:])

### Reverse the word
word = "SINGAPORE"
