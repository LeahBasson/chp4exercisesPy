#Asks the user to input a filename.
#Prints its file extension.

filename = input("Enter a filename: ")
fileExtension = filename.split(".")
print("File extension:",fileExtension[1])