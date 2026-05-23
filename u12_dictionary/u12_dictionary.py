# menu = {"food1":2.50,
#         "food2":3.50,
#         "food3":6.00}
# # price_food1 = menu["food1"] # how to retrieve value from dictionary
# print(f"the price of food1 is {price_food1}")
# menu["food1"] = 4 #if key exists, it will change its value
# print(menu)
# menu['food4'] = 9.50 #if key does not exist, it will add a new key value
# print(menu)
# how to delete key/value pair
# del menu["food1"]
# print(menu)
# food_item = input("enter food item: ")  # existence check
# if food_item in menu:
#     print(f"yes i sell {food_item}")
# else:
#     print(f"no i don't sell {food_item}")

#for loop through the list
# for key, value in menu.items():
#     print(f"{key} : ${value}")




# write a full fledge program for a menu ordering system

# in a while loop, ask the customer what they want to buy
# total = 0

# ordered = {}

# while True:
#     food = input("enter what you want to buy:")
#     if food in menu:
#         print(f"{food} is ${menu[food]}.")
#         total = total + menu[food]
#         ordered[food] = menu[food] # add to new dictionary
#     elif food == "enough":
#         break
#     elif food not in menu:
#         print("food is not in menu.")
# # print(f"your total cost of food is ${total}")
# for food, price in ordered.items():
#     print(f"you ordered {food}: ${price}")
    
    
    
# if item exist, say the price

# else say " i don t sell the item"

# keep asking until the customer say "enough"

# bonus: total up all the items the customer order.
# and print out the total for customer to pay money







student_scores = {"mark":68, "joseph":85, "linda":78, "kok leong":65, "ethan":98}

# retrieve the score for mark
# mark_score = student_scores["mark"]
# print(mark_score)

# # change linda's score to 99
# student_scores["linda"] = 99
# print(student_scores)

# # add a new student kevin, 45
# student_scores["kevin"] = 45
# print(student_scores)

# # delete mark from dictionary
# del student_scores["mark"]
# print(student_scores)

student_scores = {"mark":68, "joseph":85, "linda":78, "kok leong":65, "ethan":98}

# what is the average score of the students in this class?
total = 0
count = 0
for name, score in student_scores.items():
    total = total + score
    count += 1
student_average = total/len(student_scores)
print(student_average)

# what is the highest score, and who score the highest.
highest = 0
highest_name = ""
for name, score in student_scores.items():
    if score > highest:
        highest = score
        highest_name = name
print(f"{highest_name} : {highest}")
    
