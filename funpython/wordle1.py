
#------------------------------------------------
# 1. Read and process the dataset

# Open the file FiveLetterWords.txt.
# Read the entire line from the file.
# Split the line using commas (,) to obtain a list of individual words.
#------------------------------------------------

with open("FiveLetterWords.txt","r") as fobj:
    words = fobj.read()
    splitwords = words.split(",")
# print(splitwords)



#------------------------------------------------
# 2. Count distinct vowels in each word

# For every word in the list:
# Count how many of the vowels a, e, i, o, u appear in the word.
# Each vowel is counted only once, even if it appears multiple times.
# Example:
# "eerie" contains only 2 distinct vowels (e and i).
#------------------------------------------------
# vowels = ["a","e","i","o","u"]
# for word in splitwords:
#     vcount = []
#     for char in word:
#         if char in vowels and char not in vcount:
#             vcount.append(char)

#     numvowels = len(vcount)
#     print(f"{word},Num of unique vowels: {numvowels}")




#------------------------------------------------
# 3. Categorise the words

# Create five separate lists to classify words:
# vowel1
# vowel2
# vowel3
# vowel4

# Append each processed word into the correct list based on its vowel count.
#------------------------------------------------
vowels = ["a","e","i","o","u"]
v1 = []
v2 = []
v3 = []
v4 = []
for word in splitwords:
    vcount = []
    for char in word:
        if char in vowels and char not in vcount:
            vcount.append(char)

    numvowels = len(vcount)
    print(f"{word},Num of unique vowels: {numvowels}")

    if numvowels == 1:
        v1.append(word)
    elif numvowels == 2:
        v2.append(word)
    elif numvowels == 3:
        v3.append(word)
    else:
        v4.append(word)




#------------------------------------------------
# 4. Display the results

# At the end of the program:

# Print all words that contain 4 or more distinct vowels (i.e., the contents of vowel4 and vowel5).
# Each word should be printed on its own line.
#------------------------------------------------
print(v4)




#------------------------------------------------
# 5. Additional notes

# All words in the file are lowercase.
# The file contains no additional punctuation apart from commas.
# You should not modify the text file.
# Follow proper programming style (good variable names, consistent indentation).
#------------------------------------------------