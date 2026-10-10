# A school requires a digital grade book to manage and analyze 
# student performance for a specific subject. 
# 
# You are required to develop a module that allows a teacher 
# to record student names and their respective marks in a centralized system.

# The program must ensure all entered marks fall within the 
# valid range of 0 to 100. Once the teacher has finished entering 
# all data, the program should automatically generate a class
# performance summary,providing the total student count, 
# the highest mark recorded, and the class average.

#=================================================
# Task 3.1
# Write a program that uses a while loop to collect student data. 
# The program must prompt for a Student Name and then a Mark (0 to 100). 
# The loop should terminate only when the word "quit" is
# entered for the StudentName. [2]
#=================================================
# while True:
#     student_name = input("enter student name: ")
#     if student_name == "quit":
#         break
#     else:
#         mark = int(input(f"enter {student_name}'s marks: "))







#=================================================
# Task 3.2
# Copy and paste your programfrom sub-task 3.1.
# For validation checks:
# - ensure the name is not just whitespace.
# - ensure the mark contains only numbers.
# - ensure the mark is between 0and 100 inclusive.
# If the mark is invalid,display an error message and prompt 
# the user to re-enter the mark for that specific student. [4]
#=================================================
# while True:
#     while True:
#         student_name = input("enter student name: ")

#         if student_name == "":
#             print("invalid name.")
#         else:
#             break
#     if student_name == "quit":
#             break        
#     while True:
#         mark = input("enter mark: ")
#         if not mark.isdigit():
#             print("invalid mark")
#         elif int(mark) <0 or int(mark)>100:
#             print("invalid mark range")
#         else:
#             break
    
    

    




#=================================================
# Task 3.3
# Copy and paste your program from sub-task 3.2.
# Store the validated name and mark in a dictionary named grade_book. 
# Once the loop ends, use the dictionary to display:
# - The total number of students recorded.
# - The highest mark achieved in the class.
# - The averagemark, formatted to two decimal places. [4]
#=================================================
highest = 0
total = 0
grade_book = {}
while True:
    while True:
        student_name = input("enter student name: ")

        if student_name == "":
            print("invalid name.")
        else:
            break
    if student_name == "quit":
            break        
    while True:
        mark = input("enter mark: ")
        if not mark.isdigit():
            print("invalid mark")
        elif int(mark) <0 or int(mark)>100:
            print("invalid mark range")
        else:
            grade_book[student_name] = int(mark)
            break

print(f"the number of students is {len(grade_book)}.")
for key,value in grade_book.items():
    if value > highest:
        highest = value
    total = total + value
print(f"the highest mark is {highest}.")
print(f"the average is {total/len(grade_book)}")