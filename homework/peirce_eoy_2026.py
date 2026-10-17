# Task 2
# Springdale Secondary School Green Club holds an annual 
# school-wide recycling drive.
# Students from different classes bring in recyclable materials 
# which are categorized into three types: Paper, Plastic and Metal. 
# 
# The raw collection weights (in kilograms) are logged
# in a text file named recycling data.txt on the workstation.
# You are required to develop a Python module that reads this file, processes the total
# weights collected by each class, determines the 'Recycling Champion' class 
# (the class with the highest total weight), and generatesa summay report 
# in an output text file named recycling_report.txt.

# InputFile Format (recycling_data.txt):
# The input text file has a headerrow, and each subsequentline contains 
# comma-separated values in the following format:
# Class,Paper KG,Plastic KG,Metal KG
# All weights are recorded with 1 decimal place. A sample of the input file is as follows:


# Task 2.1 [3]
# Set up the necessary file names and data tracking variables 
# at the beginning of your program:

# Define string variable for file path: filename ="recycling_data.txt",
# Initialize an empty dictionary to store each, class's total collected weight.
# • Initialize a variable to track the school's cumulative recycled weight.
# Initialize two variables to record class and respective weight of the top-performing
# class.

# Open and read recycling data.txt using with open(filename, "r"). Your code must skip the
# header row, read the data line-by-line, strip white space characters and split the comma
# separated string values into a list. 

# filename = "recycling_data.txt"
# class_total_weight = {}
# cum_recyweight = 0
# top_class = ""
# top_weight = 0

# list_recycle_data = []

# with open(filename,"r") as fobj:
#     data_list = fobj.readlines()

#     for i in range(len(data_list)):
#         if i > 0:#skipping first row

#             str_item = data_list[i].strip()
#             list_item = str_item.split(",")
#             list_recycle_data.append(list_item)
#     print(list_recycle_data)



# Task 2.2 [3]
# Copy and paste your program from sub-task 2.1
# Edit the program so that it:
# for each class, convert the Paper, Plastic, and Metal weights 
# into floating-point numbers.
# calculate the total weight collected by that specific class (the sum of Paper,
# Plastic, and Metal).
# compute a running total representing the umulative weight of materials collected
# by the entire school.

filename = "recycling_data.txt"
class_total_weight = {}
cum_recyweight = 0
top_class = ""
top_weight = 0

list_recycle_data = []

with open(filename,"r") as fobj:
    data_list = fobj.readlines()

    for i in range(len(data_list)):
        if i > 0:#skipping first row

            str_item = data_list[i].strip()
            list_item = str_item.split(",")
            list_recycle_data.append(list_item)
    print(list_recycle_data)

for item in list_recycle_data:
    thisclass = item[0]
    this_total = float(item[1]) + float(item[2]) + float(item[3])
    cum_recyweight += this_total
    class_total_weight[thisclass] = this_total
print(class_total_weight)
print(round(cum_recyweight,1))

# Task 2.3 [2]
# Copy and paste your program from sub-task 2.2
# Edit the program so that it:
# keep track of the class that has colected the highest overall total weight.
# identify and save both the class name and its total weight as the 'Recycling
# Champion'.

for thisclass, thisweight in class_total_weight.items():
    if thisweight > top_weight:
        top_weight = thisweight
        top_class = thisclass
print(f"the recycling champion is {top_class} with a weight of {top_weight}")









# Task 2.4 [2]
# Copy and paste your program from sub-task 2.3
# Edit the program so that:
# it creates and writes to an output text file named "recycling_report.txt".
# the output file must present the individual total weights for each class, the total
# weight collected by the school, and clearly highlight the Recycling Champion
# class with appropriate formatting.
# All decimal numbers must be displayed to exactly two decimalplaces.

with open("recycling_report.txt","w") as fobj2:
    for thisclass,thisweight in class_total_weight.items():
        if thisclass == top_class:
            fobj2.write(f"{thisclass} (recycling champion!) : {thisweight} \n")
        else:
            fobj2.write(f"{thisclass}:{thisweight} \n")
    fobj2.write(f"\nTotal weight collected by the sch: {round(cum_recyweight,1)} KG \n ")
    fobj2.write(f"{thisclass} (recycling champion!) : {thisweight}")