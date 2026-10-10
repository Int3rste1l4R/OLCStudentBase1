# '''
# Task 4 - 2023 Paper - Development of Program
# Open the file SPLIT_SENTENCE.py. You will see the following function that 
# takes a string of words, passed as the parameter word_string, splits it 
# into individual words and stores these words in a list. 
# It returns the list of words. 

# You can assume the string does not contain punctuation marks.
# '''
def split_sentence(word_string):
    list_sentence = word_string.split(" ")
    return list_sentence

print(split_sentence("the cat is black"))
# '''
# # Task 4.1
# 10.	Save the program as CHECK_LIST_2023_<your name>_<centre number>_<index number>.py [7 marks]
# Extend the program by writing another function check_list() that searches 
# through the list of words to find a certain word. 

# If it finds the word in the list, it returns "Yes", otherwise it returns "No". 
# The variable word needs to be passed to the function. 
# The function you write must use the function split_sentence() already provided.
# Save your program.
# '''
# #---------------------------------------
# # Task 4.1 [7]
# #---------------------------------------
# # write your code here
def CHECK_LIST(word,wordstring):
    word_list = split_sentence(wordstring)
    if word in word_list:
        return "Yes"
    else:
        return "No"

print(CHECK_LIST("red","the cat is black"))











# '''
# # Task 4.2
# 11.	Save your program as REVERSE_2023_<your name>_<centre number>_<index number>.py [7 marks]
# Extend your program by writing another function reverse_sentence() 
# that reverses the words in the string and returns the whole string reversed, 
# with spaces between the words. 

# For example, 
# "the cat sat on the mat" would return: "mat the on sat cat the". 

# The function you write must use the function split_sentence() already provided. 
# You must not use the slice operator or the reverse function available in Python. 
# Your program does not need to consider any spaces before or after 
# the reversed sentence. Save your program.
# '''
# # write your code here

# #---------------------------------------
# # Task 4.2 [7]
# #---------------------------------------
def reverse_sentence(words):
    word_string = split_sentence(words)
    # newlistwords = []
    # for i in word_string:
    #     length = len(i)
    #     newlistwords += [word_string[i]]
    # return newlistwords
    output = ""
    for w in word_string:
        output = w + " " + output
    return output
print(reverse_sentence("the cat is black"))






# '''
# # Task 4.3
# 12.	Save your program as FUNCTIONS_2023_<your name>_<centre number>_<index number>.py [6 marks]

# Extend your program by using the functions created such that it:
# •	allows the user to input a string of words (validation of this is not necessary)
# •	allows the user to input a word to search for in the string of words
# •	outputs the string of words, split into a list
# •	outputs the string of words, reversed
# •	outputs whether the word input is found in the string of words.
# Save your program.
# '''


# #---------------------------------------
# # Task 4.3 [6]
# #---------------------------------------
words = input("enter a sentence: ")
word = input("enter a word to search for: ")
wordlist = split_sentence(words)
print(wordlist)
print(reverse_sentence(words))
if CHECK_LIST(word,words) == "Yes":
    print(f"{word} is in the sentence {words}")
else: 
    print(f"{word} is not in the sentence {words}")











