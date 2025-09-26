a = 88
b = 888
if b > a:
  print("b is greater than a")


a = 888
b = 888
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 88
b = 8
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#short hand

a = 8888
b = 9
if a > b: print("a is greater than b")


a = 7
b = 898
print("A") if a > b else print("B")

#nested if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


a = 33
b = 200

if b > a:
  pass #если нет условий if, чтобы избежать ошибки пишем просто pass

