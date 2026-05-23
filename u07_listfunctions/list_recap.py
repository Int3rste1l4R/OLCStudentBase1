nums = [134,43654,74,678,54,435,47,3,8,578,67,10]

# print the 3rd number in the list (what is the index? )
# print(nums[2])
# # add a new number to the list
# nums.append("21")
# print(nums)
# # delete the 2nd number from the list, i.e. index 1
# del nums[1]
# print(nums)
# # remove the number 10 from the list
# nums.remove(10)
# print(nums)
# # check if number 11 is in the list
# num = 11
# if num in nums:
#     print("number found")
# else:
#     print("number not there")

# # loop through every item in the list

# for i in nums:
#     print(i)





################################

###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 9: Summing Numbers in a List
# Write a program to calculate the sum of numbers in a list.
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

# total = 0
# for i in list1:
#     total = total + i
#     print(total)

# length = total/len(list1)
# print(length)




#------------------------------------------------------------
# Exercise 10: Finding the Maximum and Minimum
# Write a program to find the largest and smallest numbers in 
# a list using max() and min().
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]
# biggest = max(list1)
# smallest = min(list1)
# smallest = list1[0]
# for i in list1:
#     if i < smallest:
#         smallest = i
# print(smallest)

# biggest = list1[0]
# for i in list1:
#     if i > biggest:
#         biggest = i
# print(biggest)



#------------------------------------------------------------
# Exercise 11: Iterating Through a List with Indices
# Write a program to print each element in a list with its index.
fruits = ["apple", "banana", "cherry"]





#------------------------------------------------------------
# Exercise 12: Reversing a List
# Write a program to reverse the order of elements in a list.
cities = ["New York", "London", "Paris", "Tokyo"]
# reversecities = cities[::-1]
# print(reversecities)
# reverse = []
# for city in cities:
#     reverse.insert(0,city)
# print(reverse)




#------------------------------------------------------------
# Exercise 13: Sorting a List
# Write a program to sort a list of numbers in ascending order.
list1 = [2944,4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]
ascending = sorted(list1)
descending = sorted(list1, reverse = True)
print(ascending)
print(descending)





#------------------------------------------------------------
# Exercise 14: Removing Specific Index with del()
# Write a program to remove the third element in a list using del.
# Then print the updated list.
list1 = [2944,4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]





#------------------------------------------------------------