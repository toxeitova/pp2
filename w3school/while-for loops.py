i = 1
while i < 6:
  print(i)
  i += 1

#break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) #3 is missing

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x) # по отдельности буквы выйдут

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) #apple

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) #skip banana

for x in range(6):
  print(x) #from 0 to 5

for x in range(2, 30, 3):
  print(x)   #2 5 8 - 29

for x in range(6):
  print(x)
else:
  print("Finally finished!") #when the loop is finished else , the else block will NOT be executed if the loop is stopped by a break statement

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y) #red apple, red banana, red cherry ...

for x in [0, 1, 2]:
  pass #если пустой


