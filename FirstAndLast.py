#Asks the user for their name.
#Prints the first and last character of it.
#Then,modify it to also print the second and second-to-last characters.

name = input("Enter your name: ")
print("First letter: ",name[0]) #name[0::-1]
print("Last letter: ",name[-1])
print ("Second letter: ",name[1])
print ("Second last letter: ",name[-2])

# Print the first 2 and the last 2 characters.
print ("First 2 letters: ",name[0:2])
print ("Last 2 letters: ",name[-2:]) # :-2 , the colon in the front prints everything except the last 2.