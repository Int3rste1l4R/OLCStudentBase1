# longest = 0
# with open('exercise.txt','r') as fobj:
#     contents = fobj.read().split()

# for word in contents:
#     if len(word) > longest:
#         longest = len(word)
# print(f"the longest word is {word}")


word_vowel = []
counter = 0
with open('words.txt','r') as f:
    contents = f.read().split()
    vowel_list = ['a','e','i','o','u','y']
    for word in contents:
        for letter in word:
            if letter in vowel_list:
               counter+=1
               if counter >=6:
                   word_vowel.append(word)
                   counter = 0
                   break
        counter = 0
    print(word_vowel)



# (56 Lines)
# There is at least one word in the English language that contains each of the vowels
# a, e, i, o, u and y exactly once and in order. Write a program that searches a file
# containing a list of words and displays all of the words that meet this constraint. The
# user will provide the name of the file that will be searched. Display an appropriate
# error message and exit the program if the user provides an invalid file name or if
# something else goes wrong while searching for words with six vowels in order.


# Exercise 1: Student Name Tag
# During orientation, each student receives a printed name tag.
#
# Write a function print_name_tag(name, class_name) that prints:
# Welcome 
# Class: 
#
# Example function call:
# print_name_tag("Alicia", "3E1")
#
# Sample output:
# Welcome Alicia
# Class: 3E1
def func(name,class_name):
    return f"welcome {name}\nclass: {class_name}"
print(func("jovan","3EMPATHY"))