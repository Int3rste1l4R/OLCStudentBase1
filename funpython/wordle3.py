with open("FiveLetterWords.txt","r") as fobj:
    words = fobj.read() # return string of words
    splitwords = words.split(",")

 
# 2. Count letter occurrences across words


# You will analyse all 26 lowercase letters of the English alphabet:
# a b c d e f g h i j k l m n o p q r s t u v w x y z

# For each letter:
# Count how many different words contain that letter at least once.
# For example, if the letter ‘e’ appears in 3,000 different words, 
#    its count is 3,000.
# Repeated letters inside the same word (e.g. "seems") should still 
#    contribute only 1 to that word’s count for ‘e’.
# Store these counts in a suitable data structure so that each 
#     letter can be associated with its count.
alpha = [["a",0],["b",0],["c",0],["d",0],["e",0],["f",0],["g",0],["h",0],["i",0],["j",0],["k",0],["l",0],["m",0],["n",0],["o",0],["p",0],["q",0],["r",0],["s",0],["t",0],["u",0],["v",0],["w",0],["x",0],["y",0],["z",0]]
for word in splitwords:
    for i in range(len(alpha)):
        temp = alpha[i]
        if temp[0] in word:
            temp[1] += 1
        temp = alpha[i]
# print(alpha)

# find the letter with the highest count
largest = 0
for alphanumlist in alpha: # ["a",0]
    temp = alphanumlist[1] # 0
    if temp > largest:
        largest = temp
print(largest)




alphalist = [["a",0],["b",0],["c",0],["d",0],["e",0],["f",0],["g",0],["h",0],["i",0],["j",0],["k",0],["l",0],["m",0],["n",0],["o",0],["p",0],["q",0],["r",0],["s",0],["t",0],["u",0],["v",0],["w",0],["x",0],["y",0],["z",0]]

for word in FiveLetterList:
    for i in range(len(alphalist)):
        templetter = alphalist[i]
        if templetter[0] in word:
            templetter[1] = templetter[1] + 1

        alphalist[i] = templetter

# print(alphalist)

# bubble sort
for i in range(len(alphalist)):
    for j in range(0, len(alphalist)- i - 1):
        if alphalist[j][1] < alphalist[j+1][1]:
            alphalist[j],alphalist[j+1] = alphalist[j+1], alphalist[j]

print(alphalist)