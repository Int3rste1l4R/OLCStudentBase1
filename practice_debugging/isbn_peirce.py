# The task is to identify and correct errors in the program code 
# sot hat the program works according
# to the International Standard Book Number (ISBN-10)rules.

# Rules for a 10-digit ISBN:
# Length: Must be exactly 10 characters long.
# Format: The first 9characters must be digits only.

# Calculation:
# Multiply the 1st digit by 10, 2nd by 9... down to the 9th digit 
# multiplied by 2.
# Sum these products and find the remainder when divided by 11.
# Subtract the remainder from 11.
# Check Digit (LastCharacter):
# If the result is 11, the last character must be '0'.
# If the result is 10, the last character must be 'X.
# Otherwise, the last character must match the calculated result.
# There are several syntaX errors and logic errors in the program.


def check_isbn(isbn): #1.missing colon
    if len(isbn) != 10: #2.should be != 10
        return False
    result = 0
    for i in range(9): #3.exclude last character
        char = isbn[i]
        if not char.isdigit(): #4.is digit has no underscore
            return False
        result += (10 - i) * int(char)#5.need to add the result
        print(f"result: {result} i: {i} char:{char}") #debugging

    result = 11 - (result % 11) #6.should be % modulus
    print(f"result: {result}") #debugging
    if result == 11:
        return isbn[-1] == '0'
    if result == 10:
        return isbn[-1] == 'X' #7.supposed to be '=='
    return isbn[-1] == str(result) #8.cast result to str

while True:
    isbn = input("Enter ISBN: ")
    if check_isbn(isbn): #9.function name is check_isbn
        print("Valid ISBN entered!") #10.supposed to have indent for loop
        break
    print("Invalid ISBN entered! Try again.")





    # backup
#     def check_isbn(isbn)
#     if len(isbn) == 10:
#         return False
#     result = 0
#     for i in range(10):
#         char = isbn[i]
#         if not char.is_digit():
#             return False
#         result = (10 - i) * int(char)

#     result = 11 - (result / 11)

#     if result == 11:
#         return isbn[-1] == '0'
#     if result == 10:
#         return isbn[-1] = 'X'
#     return isbn[-1] == result

# while True:
#     isbn = input("Enter ISBN: ")
#     if checkisbn(isbn):
#     print("Valid ISBN entered!")
#         break
#     print("Invalid ISBN entered! Try again.")