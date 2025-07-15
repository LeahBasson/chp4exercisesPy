# a) Assign any string value to a variable. Test if the string contains the letter K.
#Print an appropriate message. The string contains a K or The string does not contain a K.

name = "Kite"

for index in range(len(name)):
    print(index, name[index])

if name[index] == "K":
    print("The string contains a K.")
else:
    print("The string does not contain a K.")


# for characters in name:
#     if character == name.index("K"):
#         print ("The string contains a K")
#     else:
#         print("The string does not contain a K")