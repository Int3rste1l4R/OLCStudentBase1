# Exercise 12: Distance Between Two Points on Earth  

# (27 Lines)  

# The surface of the Earth is curved, and the distance between degrees of longitude varies with latitude. 
# As a result, finding the distance between two points on the surface of the Earth 
# is more complicated than simply using the Pythagorean theorem.  

# Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s surface. 
# The distance between these points, following the surface of the Earth, in kilometers is:  

# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))  

# The value 6371.01 in the previous equation wasn’t selected at random. 
# It is the average radius of the Earth in kilometers.  

# Create a program that allows the user to enter the latitude and 
# longitude of two points on the Earth in degrees. Your program should display
#  the distance between the points, following the surface of the earth, in kilometers.  

# www.allitebooks.com 

# Exercise 12: Distance Between Two Points on Earth 7  

# Hint: Python’s trigonometric functions operate in radians. 
# As a result, you will need to convert the user’s input from degrees to radians 
# before computing the distance with the formula discussed previously. 
# The math module contains a function named radians which converts from degrees to radians.  

# https://docs.python.org/3/library/math.html

# SG is 1.3521 and 103.8198
# TKY is 35.6895 and 139.6917

# import math

# # math.acos(x)
# # math.cos(x)
# # math.sin(x)
# # math.radians(x)

# lat1 = float(input("enter latitude of position 1: "))
# lon1 = float(input("enter longtitude of position 1: "))

# lat2 = float(input("enter latitude of position 2: "))
# lon2 = float(input("enter longtitude of position 2: "))

# lat1 = math.radians(lat1)
# lon1 = math.radians(lon1)

# lat2 = math.radians(lat2)
# lon2 = math.radians(lon2)

# distance = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

# print(f"The distance between the two points is {round(distance,2)}.")



# Exercise 27: Body Mass Index  

# (14 Lines)  

# Write a program that computes the body mass index (BMI) of an individual. 
# Your program should begin by reading a height and weight from the user. 
# Then it should use one of the following two formulas to compute the 
# BMI before displaying it.  

# If you read the height in meters and the weight in kilograms then 
# body mass index is computed using this slightly simpler formula:  

# BMI = weight / height × height .  
height = float(input("enter your height in meters: "))
weight = float(input("enter your weight in kg: "))
BMI = weight/(height*height)
print(f"your BMI is {round(BMI,3)}.")