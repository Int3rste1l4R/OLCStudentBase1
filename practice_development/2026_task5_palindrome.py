# 5.1
def midpoint(word):
    if word == "":
        return 0
    else:
        mid_index = len(word)//2
        if len(word) % 2 == 0:
            return mid_index - 1
        else:
            return mid_index
# print(midpoint("melon"))
# print(midpoint("pineapples"))

# 5.2
def palindrome(word):
    mid_index = midpoint(word)
    if mid_index == 0:
        return "no word entered"
    
    if len(word) %2 == 0: # even length
        count1 = 0
        count2 = 1
        for i in range(mid_index + 1):
            if word[mid_index - count1] != word[mid_index + count2]:
                return "not palindrome"
            count1 += 1
            count2 += 1
        return "palindrome"
    else: # odd length
        for i in range(1,mid_index + 1):
            if word[mid_index - i] != word[mid_index + 1]:
                return "not palindrome"
        return "palindrome"


# start 5.3

word = input("enter a word: ")
middle = midpoint(word)

mid_index = midpoint(word)
palin = palindrome(word)
if palin == "not palindrome":
    new_palin = word + word[::-1]
    print(new_palin)
else:
    print(f"word is {palin}")