# Wordle Positional Letter Analysis

# Task: Determining the Most Common Position of Each Vowel

# You are given a text file named FiveLetterWords.txt, containing 5,757 English words.
# All words are five letters long and appear on one line, separated by commas.

# In the previous assignment, you identified which words contained the 
# highest number of distinct vowels.

# In this assignment, your focus is on positional frequency—that is,
# where in the word each vowel tends to appear most often.

# Understanding letter positions is a useful strategy in Wordle.
# For example, if you already know the secret word contains the letter ‘u’, 
# and analysis shows that ‘u’ appears most frequently in position 2, 
# you can prioritise guesses with ‘u’ in that position.

# Task Requirements

#----------------------------------------
# 1. Read and process the dataset

# Open the file FiveLetterWords.txt.
# Read the entire line.
# Split the line using commas (,) to obtain a list of individual 5-letter words.
#----------------------------------------
with open("FiveLetterWords.txt","r") as fobj:
    words = fobj.read()
    splitwords = words.split(",")



#----------------------------------------
# 2. Analyse vowel positions

# A vowel is one of the following:
# a, e, i, o, u

# For each vowel:

# Create a list of five counters, each representing a position in a 5-letter word.
# Example:
# lstCount = [0, 0, 0, 0, 0]
# where index 0 corresponds to position 1, index 1 to position 2, and so on.
# Loop through every word in the dataset.
# Each time the vowel appears in the word, increment the counter for the correct position.
# For example, if the vowel is u and the word is "sunny":

# 'u' appears in position 2 → increment the second counter.
#----------------------------------------
vowels = ["a","e","i","o","u"]
alist_count = [0,0,0,0,0]
for word in splitwords:





#----------------------------------------
# 3. Display the results

# After processing all words:

# Print the positional frequency list for each vowel.
# Follow this output format:
# u is [75, 534, 313, 154, 13]

# Interpretation of this example:

# ‘u’ appears as the 1st letter → 75 times
# 2nd letter → 534 times
# 3rd letter → 313 times
# 4th letter → 154 times
# 5th letter → 13 times
#----------------------------------------






#----------------------------------------
# 4. Bonus Task (Optional)

# Extend your program so that it computes positional frequencies for all letters of the alphabet, not just vowels.
# Output should follow the same list format.
#----------------------------------------
