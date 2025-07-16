# a) Assign any string value to a variable.
#Test if the string contains the letter K.
#Print an appropriate message. The string contains a K or The string does not contain a K.

name = "Leah"

search_results = name.find("K")

if search_results > -1:
    print("The string contains a K.")
else:
    print("The string does not contain a K.")