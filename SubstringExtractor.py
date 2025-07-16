#Takes a sentence from the user.
#Extracts and prints a substring using start and end indices entered by the user.
#The user enters the text, then the start index, then the end index.

text = input("Enter a sentence: ")
start_index = int(input("Enter start index: "))
end_index = int(input("Enter end index: "))

print("Substring:",text[start_index:end_index])