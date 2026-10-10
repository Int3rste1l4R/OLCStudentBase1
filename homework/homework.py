# On some basic cell phones, text messages can be sent using the numeric keypad.
# Because each key has multiple letters associated with it, multiple key presses are
# needed for most letters. Pressing the number once generates the first letter on the key.
# Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth
# character listed for that key.

# Key Symbols
# 1 . , ? ! :
# 2 A B C
# 3 D E F
# 4 G H I
# 5 J K L
# 6 M N O
# 7 P Q R S
# 8 T U V
# 9 W X Y Z
# 0 space

# Write a program that displays the key presses that must be made to enter a text message
# read from the user. Construct a dictionary that maps from each letter or symbol to the
# key presses. Then use the dictionary to generate and display the presses for the user’s
# message. For example, if the user enters Hello, World! then your program should output
# 4433555555666110966677755531111. Ensure that your program handles both
# uppercase and lowercase letters. Ignore any characters that aren’t listed in the table
# above such as semicolons and brackets.
text = "a,b!c." # sample text e.g. Hello world
dictionary = {".":"1",
              ",":"11",
              "?":"111",
              "!":"1111",
              "A":"2",
              "B":"22",
              "C":"222"}

# find the value:
# dictionary["1"] # .


# loop through all characters in the text
for char in text:
    ### for each text, find the dictionary value.

    number = dictionary[char.upper()]

    output = ""
    output += number
    print(output)















# Morse code is an encoding scheme that uses dashes and dots to represent numbers
# and letters. In this exercise, you will write a program that uses a dictionary to store the
# mapping from letters and numbers to Morse code. Use a period to represent a dot, and
# a hyphen to represent a dash. The mapping from letters and numbers to dashes and
# dots is shown in Table 6.1.
# Your program should read a message from the user. Then it should translate each letter
# and number in the message to Morse code, leaving a space between each sequence of
# dashes and dots. Your program should ignore any characters that are not letters or
# numbers. The Morse code for Hello, World! is shown below:

# .... . .-.. .-.. --- .-- --- .-. .-.. -..






















# In a Canadian postal code, the first, third and fifth characters are letters while the
# second, fourth and sixth characters are numbers. The province can be determined from
# the first character of a postal code, as shown in the following table. No valid postal
# codes currently begin with D, F, I, O, Q, U, W, or Z.

# The second character in a postal code identifies whether the address is rural or
# urban. If that character is a 0 then the address is rural. Otherwise it is urban.
# Create a program that reads a postal code from the user and displays the province
# associated with it, along with whether the address is urban or rural. For example, if the
# user enters T2N 1N4 then your program should indicate that the postal code is for an
# urban address in Alberta. If the user enters X0A 1B2 then your program should indicate
# that the postal code is for a rural address in Nunavut or Northwest Territories. Use a

# dictionary to map from the first character of the postal code to the province name.
# Display a meaningful error message if the postal code begins with an invalid character.




















# While the popularity of cheques as a payment method has diminished in recent years,
# some companies still issue them to pay employees or vendors. The amount being paid
# normally appears on a cheque twice, with one occurrence written using digits, and the
# other occurrence written using English words. Repeating the amount in two different
# forms makes it much more difficult for an unscrupulous employee or vendor to modify
# the amount on the cheque before depositing it.
# In this exercise, your task is to create a function that takes an integer between 0
# and 999 as its only parameter, and returns a string containing the English words for that
# number. For example, if the parameter to the function is 142 then your function should
# return “one hundred forty two”. Use one or more dictionaries to implement your solution
# rather than large if/elif/else constructs. Include a main program thatreads an integer from
# the user and displays its value in English words.










# The notion of anagrams can be extended to multiple words. For example, “William
# Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
# spacing are ignored.
# Extend your program from Exercise 135 so that it is able to check if two phrases
# are anagrams. Your program should ignore capitalization, punctuation marks and
# spacing when making the determination.