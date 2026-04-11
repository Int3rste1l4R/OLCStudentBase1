# for i in range(5):
#     print(i)





###################################################
# Part 1: Learning Exercises
# Exercise 1: Simple Loop with range(stop)
# Write a program to print "Welcome to Python!" 5 times.
# Use range(stop) to repeat the message.
# for i in range(5):
#     print("welcome to python")


# #------------------------------------------------------------
# # Exercise 2: Printing Numbers with range(stop)
# # Write a program to print numbers from 0 to 4 using range(stop).
# # Example: Output = 0, 1, 2, 3, 4.



# #------------------------------------------------------------
# # Exercise 3: Counting with range(start, stop)
# # Write a program to print numbers from 10 to 15.
# # Use range(start, stop) to set the range.
# # Example: Output = 10, 11, 12, 13, 14, 15.
# for i in range(10,16):
#     print(i)


# #------------------------------------------------------------
# # Exercise 4: Using range(start, stop, step)
# # Write a program to print even numbers from 2 to 10.
# # Use range with a step value.
# # Example: Output = 2, 4, 6, 8, 10.
# for i in range(2,11,2):
#     print(i)


# #------------------------------------------------------------
# # Exercise 5: Printing Numbers in Reverse
# # Write a program to print numbers from 10 to 1.
# # Use range(start, stop, step) with a negative step value.
# # Example: Output = 10, 9, 8, ..., 1.
# for i in range(10,0,-1):
#     print(i)


# #------------------------------------------------------------
# # Exercise 6: Summing Numbers in a Range
# # Write a program to calculate the sum of numbers from 1 to 10.
# # Use range(start, stop) and a loop to add the numbers.
# # # Example: Output = 55.
# total = 0
# for i in range(1,11):
#     total= total+i
# print(total)



# #------------------------------------------------------------
# # Exercise 7: Printing a Simple Pattern
# # Write a program to print the following pattern:
# # *
# # **
# # ***
# # ****
# # *****
# total=""
# for i in range(5):
#     total = total+"*"
#     print(total)

# for i in range(1, 6):
#     print("*" * i)


###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 8: Printing Odd Numbers
# Write a program to print all odd numbers from 1 to 15.
# Use range(start, stop, step) to skip even numbers.
# Example: Output = 1, 3, 5, ..., 15.
# for i in range(1,16,2):
#     print(i)


#------------------------------------------------------------
# Exercise 9: Multiplying Numbers
# Write a program to print the first 12 multiples of 7.
# Use range(start, stop, step).
# Example: Output = 7, 14, 21, 28, 35.

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# ...

# num = 7
# for i in range(1,13):
#     print(f"{num} x {i} = {num*i}")
#------------------------------------------------------------
# Exercise 10: Repeating a Phrase
# Write a program to print "I love Python!" 3 times.
# Use range(stop) to repeat the phrase.






#####
# Write a cheer program
# word = "SINGAPORE"
# for c in word:
#     print(f"give me a {c}!")
# print(f"{word}!!!")


#------------------------------------------------------------
# Exercise 7: Loop Through a String (characters)
# Count the vowels in the string and print the total.
# Data:
# text = "the quick brown fox jumps over the lazy fox."
# Vowels: a, e, i, o, u (case-insensitive)
# # Example: Output = 7
# text = "the quick brown fox jumps over the lazy fox."
# numb_count = 0
# for v in text:
#     if v in "aeiou":
#         numb_count = numb_count+1
# print(numb_count)



#------------------------------------------------------------
# Exercise 8: Loop Through a String Using Index
# Print each character with its index in the format: index:char
# Data:
# name = "Python"
# Example: 
# 0:P
# 1:y
# 2:t
# 3:h
# 4:o
# 5:n
name = "python"
for i in range(len(name)):
    print(f"{i+1}:{name[i]}")