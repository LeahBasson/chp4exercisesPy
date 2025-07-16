#Asks the user for a word.
#Prints each character along with its index using a loop.

word = input("Enter a word: ")

for index in range(len(word)):
    print("Character at index", index,"is", word[index])
    
