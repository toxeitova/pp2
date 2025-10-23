import re
text = input("Enter a string: ")

if re.match(r'^[a-z]', text):
    print("The string starts with a lowercase letter.")
elif re.match(r'^[A-Z]', text):
    print("The string starts with an uppercase letter.")
else:
    print("The string does not start with a letter.")


import re
text = input("Enter a sentence: ")
if re.match(r'^[A-Z]', text):
    print("The sentence starts with a capital letter.")
else:
    print("The sentence does not start with a capital letter.")

import re
text = input("Enter a sentence: ")
if re.match(r'^\d', text):
    print("The sentence starts with a number.")
else:
    print("The sentence does not start with a number.")

import re
text = input("Enter a sentence: ")
if re.match(r'^[abcABC]', text):
    print("The sentence starts with a, b, or c (any case).")
else:
    print("The sentence starts with another letter.")


import re
text = input("Enter a sentence: ")
if re.search(r'\.$', text):
    print("The sentence ends with a period.")
else:
    print("The sentence does not end with a period.")

import re
text = input("Enter a sentence: ")
if re.search(r'\?$', text):
    print("The sentence ends with a question mark.")
else:
    print("The sentence does not end with a question mark.")

import re
text = input("Enter a word: ")
if re.fullmatch(r'[A-Za-z]+', text):
    print("Contains only letters.")
else:
    print("Contains other characters too.")

import re
text = input("Enter a sentence: ")
if re.search(r'[A-Z]', text):
    print("The sentence contains uppercase letters.")
else:
    print("No uppercase letters found.")


import re
text = input("Enter a sentence: ")
if re.match(r'^[A-Z].*\.$', text):
    print("This looks like a proper sentence.")
else:
    print("This sentence may not be properly formatted.")
