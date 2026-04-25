# Exercise 7: Multiplication Table with While Loop
# Write a program to print the multiplication table of 7 up to 10.
# Example: 7 x 1 = 7, ..., 7 x 10 = 70.
# multiple = 1
# while multiple <= 10:
#     ans =7 * multiple
#     print(f"7 x {multiple} = {ans}")
#     multiple = multiple + 1
    




#------------------------------------------------------------
# Exercise 8: Sum of Even Numbers
# Write a program to calculate the sum of numbers between 1 
# # and 20 using a while loop. Example: Output = 110.
# number =1
# totalsum=0
# while number <=20:
#     totalsum=totalsum+number
#     number+=1
#     print(totalsum)




#------------------------------------------------------------
# Exercise 10: Input Validation for a Password
# Write a program that keeps asking the user to enter a password.
# If the password is correct, print "Access granted."

# correct = "pass123"

# # password = input("What is your password? ")
# # if password != correct:
# #     print("incorrect, try again")
# # else:
# #     print("correct password, access granted")

# ### input validation >>> 
# while True:
#     password = input("What is your password? ")
#     if password != correct:
#         print("incorrect, try again")
#     else:
#         print("correct password, access granted")
#         break








#------------------------------------------------------------
# Exercise 6: While True + break 
# Repeatedly ask for integers and add them to a total.
# Stop when user enters "END" (case-insensitive).
# Print total after stopping.
# Sample Inputs: 10, 20, 5, END
# Example Output: Total = 35
#------------------------------------------------------------
# total = 0
# while True:
#     number = input("give me a number ")
    
#     if number == "end":
#         print(total)
#         break
#     total = total + int(number)







#------------------------------------------------------------
# Exercise 7: While True  (Skip Negatives)
# Repeatedly accept integers. If number is negative, skip and ignore it.
# Stop on 0. Print count of valid positives and their sum.
# Sample Inputs: -3, 5, 12, -1, 4, 0
# Example Output: Count = 3, Sum = 21
#------------------------------------------------------------
# sume = 0 
# count = 0

# while True:
#     nuber= int(input("give me a number: "))
#     if nuber < 0:
#         continue
#     elif nuber == 0:
#         print(f"count = {count}, sum = {sume}")
#         break
#     else:
#         sume=sume+nuber
#         count += 1






#------------------------------------------------------------
# Exercise 8: Presence Check (Non-Empty String)
# Ask for a name. Keep asking until a non-empty name is entered.
# Then greet the user.
# Sample Input: "" -> "   " -> "Alex"
# Example Output: Hello, Alex!
#------------------------------------------------------------





#------------------------------------------------------------
# Exercise 9: Length Check (Username)
# Ask for a username that must be 5 to 12 characters long.
# Keep prompting until valid, then print "Username accepted".
# Sample Inputs: "ab" (invalid), "student01" (valid)
#------------------------------------------------------------
# username=input("input a username: ")
# if len(username)


while True:
    user = input("what is username: ")
    if len(user) <=12 and len(user) >=5:
        print("username accepted")
        break
    else:
        print("unaccepted")