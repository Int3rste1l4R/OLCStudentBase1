# TASK1_<your name>_<class>_<index number>.ipynb
# A high-security government facility requires a digital entry system that validates a visitor's NRIC before granting access. You are required to develop the input validation module for this system.
# Write a program that uses an interactive while loop to prompt the user to enter their NRIC. The program must validate the input string based on the following rules:

# the input must not be empty and must be exactly 9 characters long.
# the first character and the last character must be alphabet and uppercase letters.
# the seven characters in the middle must be digits only.

# If the NRIC fails any of the validation checks, the program must display the message: "Invalid NRIC format. Please try again." and repeat the prompt. 
# The loop must only terminate once a valid NRIC has been entered.
# For this task, add a comment using the hash symbol '#' at the beginning of your code to indicate the task that the program code belongs to. For example:
# textIn [1]: # Task 1
#         Program code
# Output:
# The following is a simple program that asks the user to key in a valid NRIC.
# textnric = input("Enter your NRIC: ")
# print("Your NRIC entered is {}".format(nric))
# Edit the program so that the necessary validation checks will be deployed.
# Below are some samples of how the program should behave when it is working as intended:


# Sample 1
# textEnter your NRIC: s1234567a
# Invalid NRIC format. Please try again.
# Re-enter your NRIC: S1234567A
# Your NRIC entered is S1234567A


# Sample 2
# textEnter your NRIC: 1234567
# Invalid NRIC format. Please try again.
# Re-enter your NRIC:
# Invalid NRIC format. Please try again.
# Re-enter your NRIC: SG123456A
# Invalid NRIC format. Please try again.
# Re-enter your NRIC: S1234567A
# Your NRIC entered is S1234567A
# [10]

# while True:
#     NRIC = input("enter NRIC: ")
#     valid = (
#         len(NRIC) == 9
#         and NRIC[0].isupper()
#         and NRIC[-1].isupper()
#         and NRIC[1:8].isdigit() 
#         )
#     if valid:
#         print("valid NRIC.")
#         break
#     else:
#         print("inavlid nric. Try again")




# def check_isbn(isbn): #error 1
#     if len(isbn) != 10:#error 2
#         return False 

#     result = 0
#     for i in range(9): #error 3
#         char = isbn[i]
#         if not char.isdigit(): #error 4
#             return False
#         result += (10 - i) * int(char) #error 9

#     result = 11 - (result % 11)

#     if result == 11:
#         return isbn[-1] == '0'
#     if result == 10:
#         return isbn[-1] == 'X' #error 5
#     else: #error 10
#         return isbn[-1] == str(result)

# while True:
#     isbn = input("Enter ISBN: ")
#     if check_isbn(isbn): #error 6
#         print("Valid ISBN entered!") #error 7
#         break
#     else:    #error 8
#         print("Invalid ISBN entered! Try again.")



# Task 3.2
grade_book = {}
while True:
    name = input("Enter student name: ")
    if name == "quit":
        break

    if name.strip() == "":
        print("Invalid name. Please try again.")
        continue

    while True:
        mark_text = input("Enter mark: ")
        if not mark_text.isdigit():
            print("Invalid mark. Please re-enter the mark.")
            continue
        mark = int(mark_text)
        if mark < 0 or mark > 100:
            print("Invalid mark. Please re-enter the mark.")
            continue
        break
    grade_book[name] = mark
    print(name, mark)  # later you will store this in grade_book

    print("Total students:", len(grade_book))
    print("Highest mark:", max(grade_book.values()))
    average = sum(grade_book.values()) / len(grade_book)
    print("Average mark: {:.2f}".format(average))