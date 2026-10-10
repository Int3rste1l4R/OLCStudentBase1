# Each book is assigned a id of 10 digits. First 9 is the book's ISBN, 
# while the last digit is used to validate the ISBN,

# 1. Multiply the first digit by 10, the second digit by 9, 
#    the third digit by 8, and so on, up to the ninth digit multiplied by 2.
# 2. Add up the products from step 1
# 3. Take the sum from step 2 modulo 11 
# 4. Subtract the result from step 3 from 11. 
#    if the result is 11, the check digit is 0. 
#    If the result is 10, the check digit is X (i.e. Roman numeral 10). 
#    Otherwise, the check digit is the result from step 4

# Test with these
# 1541675126
# 9810185073
# 981018509X
# 9812042539
# 9810157290

# Write a program that asks the user to input a book's ID (10 digits) 
#  and validates the ISBN by checking if the 
# last digit is correct. If the input entered via the keyboard is 
# invalid, your input validation code should keep 
# trying by asking for the input to be entered again


total = 0
number = 10
while True:
    while True:
        isbn = input("enter isbn number: ") # 1
        if len(isbn) != 10:
            print("invalid.")
            isbn = input("enter another valid isbn number: ") # 1
        else:
            break
            
    for i in range(len(isbn)):
        if i < 9:
            # print(isbn[i])
            total += int(isbn[i])*number
            number -= 1      
            
    print(total)
    step_3 = total % 11
    step_4 = 11 - step_3

    if step_4 == 10:
        step_4 = 'X' 
    elif step_4 == 11:
        step_4 = 0
    print(step_4)

    # print(isbn[-1])
    if str(step_4) == isbn[-1]:
        print("valid")
        break
    else:
        print("isbn invalid.")
        # isbn = input("enter a valid isbn number: ")