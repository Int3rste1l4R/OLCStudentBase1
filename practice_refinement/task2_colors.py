# A text file shapes.txt stores a list of shapes with a comma between each value.  

# The current contents of shapes.txt are: 
# star,sphere,square,triangle 

# A text file colours.txt stores a list of colours with a comma between each value.  

# The current contents of colours.txt are: 
# red,yellow,green,blue 

# A program reads the data from each file and creates a dictionary of the values 
# so that each shape has an associated colour. The first value in each file 
# will be joined, for example, star and red. 


# The function read_values() reads the data from both files and stores 
# the data in the global dictionary data_stored.  

# The data from the shapes.txt file is used as the key and the data 
# from the colours.txt file is used as the value. 

# The function needs to work for files of any length. The files will 
# always have the same number of data values. 

# Return the dictionary data_stored

# Write program code for the function read_values(). 

# 1.read values of shapes and colours from the file
# 2. store values as string... red,yellow,green,blue  ??? how to change this into a list ??
# 3. .split() >> to split to  ### . should have 2 list

# 4. combine both into dictionary .... how ???
# 5. loop through both list using index/ count >> add to dictionary
# 6. return the dictionary
#
def read_values():
    shapes = []
    colours = []
    shape_colour = {}
    with open("colours.txt","r") as fobj:
        content = fobj.read()

    with open("shapes.txt","r") as fobj2:
        content2 = fobj2.read()

    colours = content.split(",")
    shapes = content2.split(",")
    for i in range(len(shapes)):
        shape_colour[shapes[i]] = colours[i] # adding to dictionary
    # print(shape_colour)
    return shape_colour


# call the function
shape_colour = read_values()
# print(shape_colour["star"])




##### write another function check_color()
## takes in parameter for shape
## returns the associated color for the shape
## if the shape does not exist in dictionary, it returns "None"

def check_colour(shape):
    # check if this shape is in the shape_colour dictionary
    # if yes, retrieve the color based on shape and return

    # else , return None
    if shape in shape_colour:
        colour_retrieved = shape_colour[shape]
    else:
        return None
    return colour_retrieved
shape = input("Enter a shape: ")
color_retrieved = check_colour(shape)

print(f"The color for {shape} is {color_retrieved}")