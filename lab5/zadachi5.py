import re

#1
str1 = ["a", "ab", "abb", "ac", "b", "ba"]
for s in str1:
    if re.fullmatch(r"ab*", s):
        print("Match:", s)
    else:
        print("No match:", s)
#2
str2 = ["a", "ab", "abb", "abbb", "abbbb", "abc"]
for s in str2:
    if re.fullmatch(r"ab{2,3}", s):
        print("Match:", s)
    else:
        print("No match:", s)

#3
text = "first_name, last_name, user_ID, my_variable, not_match_123"
matches = re.findall(r"[a-z]+_[a-z]+", text)
print("Found sequences:", matches)

#4
lala = "Hello there Are Some Words Like This And ALSO test"
matches = re.findall(r"[A-Z][a-z]+", lala)
print("Found sequences:", matches)

#5
str3 = ["ab", "acb", "a123b", "axyzb", "b", "ba", "abcx"]
for s in str3:
    if re.fullmatch(r"a.*b", s):
        print("Match:", s)
    else:
        print("No match:", s)

#6
text = "Hello, my name is Aru. I love coding"
new_text = re.sub(r"[ ,.]", ":", text)
print(new_text)

#7
def snake_to_camel(s):
    parts = s.split('_')                  
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
text = "this_is_lab_five"
print("Original:", text)
print("Camel case:", snake_to_camel(text))

#8
text = "SplitAtUpperCaseLettersExample"
result = re.split(r"(?=[A-Z])", text)
print("Result:", result)

#9
text = "InsertSpacesBetweenCapitalLettersNow"
result = re.sub(r"(?=[A-Z])", " ", text)
print("Result:", result.strip())

#10
def camel_to_snake(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower()
text = "thisIsLabFive"
print("Original:", text)
print("Snake case:", camel_to_snake(text))

