################################################################
# The following program collates the names and scores of students in a class.

# The program validates that the score is from 0 to 100 inclusive, 
# and also computes and outputs:

# number of scores entered
# number of students who score distinction (75 or more)
# number of students who failed (below 50)
# average score in the class
# The program allows a user to continue entering the names and scores 
# until the user enters the letter 'N' when prompted.

# There are several syntax errors and logical errors in the program.

name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0#10. count should start with 0

flag = True
while flag: #1.when running, while loop should be true
    name = input("Enter student's name: ") #5. inside of input must be string
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100: #9. should be 'and' and not 'or'
            mark_list += [mark] #3.should add mark to mark_list when mark is valid
            break
        else:
            print('Invalid mark!')
        
    count += 1
    if mark >= 75:#7. mark is distinction if 75 or more
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name]#8. should be[] not ()
    more = input('Would you like to enter another score, Y or N?: ') #2.Y and N is string
    if more == 'N':
        flag = False
average = round(sum(mark_list)/len(mark_list), 2) #6.average should be sum/how many results
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.") #4. count must be string
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))
# print(fail_list)
# print(dist_list)




# name_list = []
# mark_list = []
# dist_list = []
# pass_list = []
# fail_list = []
# count = 1

# flag = True
# while flag == False:
#     name = input('Enter student's name: ')
#     name_list += [name]
#     while True:
#         mark = int(input('Enter score of student: '))
#         if mark >= 0 or mark <= 100:
#             break
#         else:
#             print('Invalid mark!')
#         mark_list += [mark]
#     count += 1
#     if mark > 75:
#         dist_list += [name]
#     elif mark >= 50:
#         pass_list += [name]
#     else:
#         fail_list += (name)
#     more = int(input('Would you like to enter another score, Y or N?: '))
#     if more == 'N':
#         flag = False
# average = round(max(mark_list)/len(mark_list), 2)
# num_dist = len(dist_list)
# num_fail = len(fail_list)
# print("You entered " + count + " scores.")
# print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
# print("Average score is " + str(average))