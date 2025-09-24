print(89>100)
print(100<200)
print(100==100) #first example

#if-else based on condition True-False (second example)
a = 80
b = 90
if (a<b) :
    print("a is less than b")
else :
    print("a is more than b")

#bool() function
print(bool("Hello"))
print(bool(0))  #здесь проверка пусто или нет. " ", 0, none -> False автоматом

x = "Python"
y = "" 
print(bool(x))
print(bool(y))

print(bool("dictionary"))
print(bool(595))
print(bool(["math", "biology", "history"])) #все strings are true, except empty "", (). [], {}

#for example, all of them will be FALSE
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#functions can reurn a boolean
def myFunction() :
  return True
print(myFunction())

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

#python's in-built function -> isinstance()
x = 898
print(isinstance(x, int))



