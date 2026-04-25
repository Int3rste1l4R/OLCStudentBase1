# implement for loop to give 3 chances. 

# password="pasword2"
# wrong= "incorrect password"
# correct= "access granted"

# for i in range(3):
#     user = input("enter password:")
#     if user == password:
#         print(correct)
#         break # break out of the loop
#     else:
#         print(wrong)
    
# else:
#     # the code here will run on successful completion of the loop
#     print("too many attempts, try again later")


# score = int(input("what is your score? "))
# if score >= 75:
#     print("A1")
# elif score >=70:
#     print("A2")
# elif score >=65:
#     print("B3")
# elif score >=60:
#     print("B4")
# elif score >=55:
#     print("C5")
# elif score >=50:
#     print("C6")
# elif score >=45:
#     print("D7")
# elif score >=40:
#     print("E8")
# else:
#     print("F9")



# random numb guessing game, random numb 1-100, 7 chances, program will output too big, too small, or correct
import random
# randomnum = random.randint(1,100)
# print(randomnum)

# chances = 7
# guesses = 0
# for i in range(chances):
#     usernum = int(input("your guess: "))
#     if randomnum > usernum:
#         print("too small")
#     elif randomnum < usernum:
#         print("too big")
#     else:
#         print("correct number")
#         break
#     guesses= guesses + 1
#     guessesleft = chances-guesses
#     print(f"guessed {guesses}, you have {guessesleft} guesses left")
# else:
#     print("too many tries, game over")
#     print("number was", randomnum)


#=====================================================

# Exercise 9: Finding the Largest of Three Numbers
# Write a program to find the largest of three numbers.
# Example: Input = 4, 7, 2. Output = "The largest is 7."
# randomnum = random.randint(1,100)
# print(randomnum)
# num1 = randomnum
# num2 = randomnum
# num3 = randomnum
# if num1 > num2 > num3:
# # if num1 > num2 and num1 > num3:
#     print(f"largest number is {num1}")
# elif num2 > num1 > num3:
#     print(f"largest number is {num2}")
# else:
#     print(f"largest number is {num3}")




#------------------------------------------------------------
# Exercise 10: Leap Year Checker
# Write a program to check if a year is a leap year.
# Example: Input = 2024. Output = "Leap year."


# Step 1: Check if the Year is Divisible by 4
# If Y is NOT divisible by 4, it is NOT a leap year.
# If Y is divisible by 4, go to Step 2.

# Step 2: Check if the Year is a Century Year (Divisible by 100)
# If Y is divisible by 100, go to Step 3.
# Otherwise, Y is a leap year.

# Step 3: Check if the Year is Divisible by 400
# If Y is divisible by 400, then it is a leap year.
# Otherwise, it is NOT a leap year.



year = int(input("input the year: "))
commonyear = year % 4
leapyear = year % 100
leaapyear = year % 400
if commonyear != 0:
    print(f"{year} is a common year")
if leapyear != 0 and leaapyear == 0:
    print(f"{year} is a leap year")
    


# !=










#------------------------------------------------------------
# Exercise 11: Age-Based Group Assignment
# Write a program to categorize a person into groups based 
# on age: Child (0-12), Teen (13-19), Adult (20+).
# Example: Input = 15. Output = "Teen."












#------------------------------------------------------------
# Exercise 13: Even/Odd Checker
# Write a program to check if a number is even or odd.
# Example: Input = 4. Output = "Even number."
# usernum = int(input("number: "))
# checker = usernum % 2
# if checker == 1:
#     print(f"{usernum} is an odd number")
# elif checker ==0:
#     print(f"{usernum} is an even number")





#------------------------------------------------------------

# use the modulus % >> remainder after a division

