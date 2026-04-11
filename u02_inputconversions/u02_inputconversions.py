


#------------------------------------------------------------
# # Exercise 2: Understanding input() Behavior
# # Write a program to ask the user for their age and display it.
# # Example: If the user enters "15", display "Your age is 15."
# # Note: Treat the input as a string for now.

# age = input( "what is your age?")
# sentence = "your age is "+ age
# print(sentence)


# type conversion
# var1 = "dog" # string
# var2 = "cat"
# var3 = var1 + var2
# print(var3)

# # integer
# var4 = 10
# var5 = 20
# var6 = var4 + var5
# print(var6)

# var7 = var1 + var4
# print(var7)

# ask for 2 numbers
# add them up, and print out the answer

# type conversion int() str()
# num1 = int(input(" 1st number: ")) #default is always a string
# num2 = int(input(" 2nd number: "))
# num3 = num1 + num2
# sentence = f"{num1} + {num2} = {num3}"
# print(sentence)



#------------------------------------------------------------
# Exercise 8: Area of a Circle 
# Write a program to ask the user for the radius of a circle, convert it to
# a float, calculate the area using the formula (area = 3.14 * r^2), and
# display the result . Example:
# Input: radius = 7
# Output: "The area of the circle is 153.86."
# radius = input(" radius of circle ")
# area = 3.14 *int(radius)**2
# sentence = f" The area of the circle is {area} "
# print(sentence)


  ###########################################################
  # 6. Edit the program so that:
  # a)    It works for any number of gantries.
  #       The program must display a suitable input message. [1]
  ###########################################################
num_gantries = int(input("How many gantries: "))

for i in range(num_gantries):
    expressway = input("Enter name of gantry:")
    old = float(input("Enter old rate:"))
    new = float(input("Enter new rate:"))
    change = new - old
    print("Change is",change)





















# sentence = str(num1) + " + " + str(num2) + " = " + str(num3)

# string concantenation, string formatting

# option 1: print( comma)
# sentence2 = num1, "+", num2, "=", num3

# # print(sentence2)
# print(num1, "+", num2, "=", num3) # conversion

# # option 2: use + to concatenation
# sentence2 = str(num1) + " + " + str(num2) + " = " + str(num3)
# print(sentence2)

# # option 3: "".format()
# sentence3 = "{} + {} = {}".format(num1, num2, num3)
# print(sentence3)

# # option 4: f"" - f-string
# sentence4 = f"{num1} + {num2} = {num3}"
# print(sentence4)

# 10 + 20 = 30