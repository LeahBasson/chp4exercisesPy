#Asks the user for their name.
#Prints the first and last character of it.
#Then,modify it to also print the second and second-to-last characters.

name = input("Enter your name: ")
print("First letter: ",name[0::-1])
print("Last letter: ",name[-1])
print ("Second letter: ",name[1])
print ("Second last letter: ",name[-2])