#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
text = input("Enter a string here : ")
pattern = r'[A-Z][a-z]+'
matches = re.findall(pattern, text)
print("Found sequences:", matches)
