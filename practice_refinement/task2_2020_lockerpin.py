# Task 2
# The following program checks it the personal identification number (PIN) 
# entered for a locker is correct. There are 10 lockers available and 
# the correct PIN for each locker is stored in an array.

# A PIN cannot start with the digit 0.
# The program allows the user to enter the number of 
# the locker they want to open, and a PIN. 
# It checks if the PIN is correct for that locker.

# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# locker = int(input("Please enter the locker you would like to open: "))
# pin = int(input("Please enter the PIN for the locker: "))

# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else:
#     print("Incorrect PIN for that locker")

#===========================================================
# Open the file LOCKERPIN.py
# 5       Edit the program so that it converts the PIN input 
#         by the user to an integer.
# Save your program
# [1]
#___________________________________________________________

# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# locker = int(input("Please enter the locker you would like to open: "))
# pin = int(input("Please enter the PIN for the locker: "))
# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else:
#     print("Incorrect PIN for that locker")
 




#===========================================================
# 6       Edit the program to only accept a locker number 
#         between 1 and 10 (inclusive) to be input. A suitable error message 
#         must be displayed if the locker number input is not in this range. 
#         The program must loop until a valid locker number is input.
# Save your program.
# [3]
#___________________________________________________________

# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]

# while True:
#     locker = int(input("Please enter the locker you would like to open: "))
#     if locker >= 1 and locker <= 10: 
#         break
#         # locker = int(input("Please enter another locker you would like to open: "))
#     else:
#         print("invalid locker number,locker number must be from 1-10")
        

# pin = int(input("Please enter the PIN for the locker: "))

# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else:
#     print("Incorrect PIN for that locker")



 
#===========================================================
# 7       Edit the program to only accept a PIN of 4 digits 
#         to be entered by the user. A suitable error message 
#         must be displayed if an incorrect input is given. 
#         The program must loop until the PIN input is 4 digits.
# Save your program
# [3]
#___________________________________________________________

# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]

# while True:
#     locker = int(input("Please enter the locker you would like to open: "))
#     if locker >= 1 and locker <= 10: 
#         break
#         # locker = int(input("Please enter another locker you would like to open: "))
#     else:
#         print("invalid locker number,locker number must be from 1-10")
        
# while True:
#     pin = input("Please enter the PIN for the locker: ")
#     if not pin.isdigit():
#         print("pin is not in digits. Try again")
#     # else:
#     #     break
#     elif len(pin) != 4:
#         print("length of pin is not 4 digits long.")
#     else:
#         pin = int(pin)
#         break

# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else:
#     print("Incorrect PIN for that locker")



 
#===========================================================
# 8       Edit the program to loop until the user inputs both 
#         a correct locker number and the matching PIN for that locker.
# Save your program.
# [3]
#___________________________________________________________

arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]

while True:
    while True:
        locker = int(input("Please enter the locker you would like to open: "))
        if locker >= 1 and locker <= 10: 
            break
            # locker = int(input("Please enter another locker you would like to open: "))
        else:
            print("invalid locker number,locker number must be from 1-10")
            
    while True:
        pin = input("Please enter the PIN for the locker: ")
        if not pin.isdigit():
            print("pin is not in digits. Try again")
        # else:
        #     break
        elif len(pin) != 4:
            print("length of pin is not 4 digits long.")
        else:
            pin = int(pin)
            break

    if pin == arraypins[locker-1]:
        print("The locker is open.")
        break
    else:
        print("Incorrect PIN for that locker")

# while True:
#     if pin == arraypins[locker-1]:
#         print("The locker is open.")
#         break
#     else:
#         print("Incorrect PIN for that locker")