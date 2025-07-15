# a) Assign any string value to a variable. Test if the string contains the letter K.
#Print an appropriate message. The string contains a K or The string does not contain a K.

name = "Leah"

for index in range(len(name)):
    print(name[index])

if "K" in name:
    print("The string contains a K.")
else:
    print("The string does not contain a K.")


