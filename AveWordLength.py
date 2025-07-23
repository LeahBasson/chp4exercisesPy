# calculates the average length of words in a sentence entered by the user.

text = input("Enter a sentence: ")

words = text.split()
# print (words)

#Finding the sum.
sum = 0
for i in words:
    sum += len(i)
#     print(len(i))

# print(sum)
#Average calculation
ave = sum / len(words)    
print("Average word length: ",ave)    