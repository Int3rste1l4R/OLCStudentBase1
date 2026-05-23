# student_names = ["john", "mary","joseph","desmond","ali" ] # empty 

# ### Read the 4th student from a list
# print(student_names[4])

# print(student_names)

# ### change values in the list
# student_names[4] = "son"

# print(student_names)

# #### add to a list
# student_names.append("jane")
# print(student_names)

# ##### delete from the list
#  ## delete using the index position
# del(student_names[4])
# print(student_names)

#  ### removing by the item value
# student_names.remove("joseph")
# print(student_names)

# ##### how to loop through values in a list
# for name in student_names:
#     print(f"{name} is in my class")


# new_student = input("enter student name: ")

# if new_student in student_names:
#     print(f"{new_student} is in my class")
# else:
#     print(f"{new_student} is not in my class")
#     student_names.append(new_student)





#========================================================
#========================================================

# Python List Exercises: Student Names and Scores
#
# Scenario:
# You have 2 separate lists.
# One list stores student names.
# The other list stores the corresponding scores.
#
# The score at each index belongs to the student name at the same index.
#
# Example:
# names[0] matches scores[0]
# names[1] matches scores[1]
#
# Use the sample lists below for the questions.

names = [
    "Aiden", "Bella", "Charlie", "Daphne", "Ethan", "Fiona", "Grace", "Henry",
    "Isaac", "Jasmine", "Kai", "Lydia", "Mason", "Nora", "Owen", "Priya",
    "Quentin", "Rachel", "Samuel", "Tina", "Uma", "Victor", "Wendy", "Xavier",
    "Yvonne", "Zach", "Aaron", "Bianca", "Caleb", "Denise"
]

scores = [
    78, 92, 85, 92, 67, 88, 75, 81,
    90, 73, 84, 95, 69, 87, 58, 91,
    76, 83, 95, 64, 72, 89, 77, 68,
    94, 80, 61, 86, 74, 79
]

# --------------------------------------------------
# PART 1: Basic list access and membership
# --------------------------------------------------

# Q1
# Print the full names list using a for loop.
# for name in names:
#     print(name)
# # Q2
# # Print the full scores list using a for loop.
# for score in scores:
#     print(score)
# # Q3
# # Print the first student name in the list.
# print(names[0])
# # Q4
# # Print the last score in the list.
# print(scores[-1])
# # Q5
# # Find out whether "Charlie" exists in the names list.
# # Print True or False.
# nam = input("enter charlie: ")
# if nam in names:
#     print("true")
# else:
#     print("false")
# # Q6
# # Ask the user to enter a student name.
# # Check whether that student exists in the names list.
# # Print "Student found" or "Student not found".
# nam = input("enter name: ")
# if nam in names:
#     print("student found")
# else:
#     print("Student not found")






# --------------------------------------------------
# PART 2: Finding positions and matching data
# --------------------------------------------------

# Q7
# Find the index position of "Daphne" in the names list.
# Print the index./
# Q8
# Find Charlie's score by first finding Charlie's index in the names list.
# # Then use that same index to get the score from the scores list.
# charlie_pos = names.index("Charlie")
# charlie_score = scores[charlie_pos]
# charlie_name = names[charlie_pos]

# for i in range (len(charlie_pos)):
#     current_name = names[i]
#     current_score = scores[i]
#     print(f"{current_name} : {current_score}")



# Q9
# Ask the user to enter a student name.
# If the student exists, print that student's score.
# If not, print "Student not found".
# keep asking until the student exist 
while True:
    studenname = input("Enter student name: ")
    if studenname in names:
        studenname_pos = names.index(studenname)
        studenname_score = scores[studenname_pos]
        print(studenname_score)
        break
    else:
        print("doesnt exist")

        
# --------------------------------------------------
# PART 3: Working with highest and lowest values
# --------------------------------------------------

# Q11
# Find the highest score in the scores list.
# Print the highest score only.



# Q12
# Find the lowest score in the scores list.
# Print the lowest score only.

# Q13
# Find the name of the student who scored the highest mark.
# Assume there is only one highest scorer for now.

# Q14
# Find the name of the student who scored the lowest mark.
# Assume there is only one lowest scorer for now.

# Q15
# Print a sentence like this:
# "Bella scored the highest mark of 92."




# Q10
# Print every student's name together with their score.
# Example output:
# Aiden : 78
# Bella : 92
# # Charlie : 85
# for i in range(len(names)):
#     current_names = names[i]
#     current_scores = scores[i]
#     print(f"{current_names} : {current_scores}")





# string variable
# integer, float
# boolean >> True False

# List
###################################################
# Part 1: Learning Exercises

# Exercise 1: Accessing List Elements by Index
# Write a program to access and print the first, second, and last 
# elements of a list using indexing.

# fruits = ["apple", "orange", "banana","durian"] # my list
# print(fruits[2]) # retrieve a specific value from the list



# #------------------------------------------------------------
# # Exercise 2: Adding Elements to a List
# # Write a program to add an element to the end of a list using 
# # append(), and add another element at a specific index using 
# # insert().


# fruits.append("durian") # add a new item to the list, adds at the back

# fruits.insert(1, "grapes") # add at specific position





# #------------------------------------------------------------
# # Exercise 3: Using del() to Remove an Element by Index
# # Write a program to delete an element at a specific index.
# # Example: Remove the second color.

# del(fruits[1]) # deleting by the index



# #------------------------------------------------------------
# # Exercise 4: Using remove() to Remove an Element by Value
# # Write a program to remove a specific element by its value.
# # Example: Remove "green" from the list.
# # colors = ["red", "green", "blue", "yellow"]
# # colors.remove("green")  # Remove by value
# # print("Colors after removal: {}".format(colors))

# # fruits.remove("durian")

# # while True:
# #     if "durian" in fruits:
# #         fruits.remove("durian")
# #     else:
# #         break



# #------------------------------------------------------------
# # Exercise 5: Using pop() to Remove and Retrieve an Element
# # Write a program to remove the last element of a list using pop().
# # Example: Remove and print the last color.
# # colors = ["red", "green", "blue", "yellow"]
# # removed_color = colors.pop()  # Remove the last element
# # print("Removed color: {}".format(removed_color))
# # print("Colors after pop: {}".format(colors))

# lastfruit = fruits.pop() # removes last one and assign to variable
# print(fruits)




# #------------------------------------------------------------
# # Exercise 6: Modifying Elements in a List
# # Write a program to change the second element in a list to "pink."
# # colors = ["red", "green", "blue"]
# # colors[1] = "pink"  # Modify value at index 1
# # print("Modified colors: {}".format(colors))
# print(lastfruit)
# fruits[3] = "spikyfruit" # change the value
# print(fruits)

# #------------------------------------------------------------
# # Exercise 7: Membership Check
# # Write a program to check if "blue" is in the list.
# # colors = ["red", "green", "blue"]
# # if "blue" in colors:
# #     print("Blue is in the list.")
# # else:
# #     print("Blue is not in the list.")

# # validation check - existence check
# checkfruit = input("Enter a fruit name: ")
# if checkfruit in fruits:
#     print(f"{checkfruit} is in the list")
# else:
#     print(f"{checkfruit} is not in the list")

# #------------------------------------------------------------

# ##### to loop through every single item
# for i in fruits:
#     print(i)

# # for i in range(5): 