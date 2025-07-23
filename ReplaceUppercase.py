# replaces all 'a' characters in a string with '@'
# converts the whole string to uppercase.

text = input("Enter some text: ")
replaced_text = text.replace('a', '@')
modified_text = replaced_text.upper()

print("Modified text: ",modified_text)