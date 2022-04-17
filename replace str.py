mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."

# subStr = "over"

# new="on"

# str1=mainStr.replace('over',"on")
# print(str1)





str1=mainStr.split()
word=input("enter the word to remove :")

for j in str1:
    if j==word:
        str1.remove(word)

mainStr=' '.join(str1)

print(mainStr)