# checks if a given filename ends with '.txt'
# displays a corresponding message.

filename = input("Enter a filename: ")
result = filename.find(".txt")
    
if result < 0:
    print("This is not a text file.")
else:
    print("This is a text file.")
    