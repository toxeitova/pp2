#DATA TYPES
#list, allows duplicates, mutable(можно менять)
x = ["Python", "c++", "java"]
print(x)
print(type(x))

#int
y = 25
print(y)
print(type(y))

#float
z = 20.5
print(z)
print(type(z))

#complex
p = 1j
print(p)
print(type(p))

#tuple - он как list, но скобки отличаются. list можно менять, tuple no. тоже разрешает дубликаты
m = ("Tuple", "он", "не меняется")
print(m)
print(type(m))

#range
n = range(8)
print(n)
print(type(n))
print(list(n))

#dict - dictionary
l = {"name" :  "Aruzhan", "age" : 20}
print(l)
print(type(l))

#sets - unordered, no duplicates, mutable(like LIST)
numbers = {1, 1, 3, 4, 5}
print(numbers)
print(type(numbers))

#frozenset - вообще не меняется, хранит unique items
x = frozenset({"let it goo", "let it", "goo"})
print(x)
print(type(x)) 

#bool
x = False
print(x)
print(type(x)) 

#bytes - тут каждая буква превращается в свой код ASCII
x = b"Hi"
print(x)
print(type(x)) 
print(x[0]) #ASCII код 

#bytearray - изменяемый
x = bytearray(5)
print(x) #тут по дефолту все они равны 0
print(type(x)) 
x[0] = 65 #заменили первый элемент на А
print(x)

#memoryview - даёт доступ к данным в памяти без копирования
x = memoryview(bytes(5))
print(x)
print(type(x)) 

#none - значения пока нет
x = None 
print(x)
print(type(x)) 

