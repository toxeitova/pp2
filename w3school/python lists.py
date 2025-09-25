#list, allows duplicates, mutable(можно менять)
x = ["Python", "c++", "java"]
print(x)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["abc", 34, True, 40, "male"]  #list can contain different data types
print(list1)

mylist = ["apple", "banana", "cherry"] #data type of a list
print(type(mylist)) 

#list() constructor
x = "hello"
print(list(x))  # ['h', 'e', 'l', 'l', 'o']

"""List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""

thislist = ["apple", "banana", "cherry"]
print(thislist[0])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) #This will return the items from position 2 to 5. Здесь пятый не добавляется

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) #до 4 элемента

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) #c cherry do konca

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #тут манго не берется 

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#функция insert добавить в лист, именно в нужное место индексом
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 

#append() добавляет в конец list-a
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend() To append elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# можно добавить не только list
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop() 
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#тут удалит последний элемент
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del removes specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#еще может удалить полностью весь list
thislist = ["apple", "banana", "cherry"]
del thislist

#а тут просто удалит элементы и всио, без контента
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#LOOP
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])   #apple, banana, cherry по очереди выйдет


thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#List Comprehension offers the shortest syntax for looping through lists
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#sort alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) 

#numerically sort
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#sort descending 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#reverse
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) 

#copy
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# : slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#append list2 into list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#add list2 at the end of list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#listmethods
'''append() -> adds an element at the end of the list.
clear() -> removes all the elements in the list
copy() -> returns a copy of the list
count() -> returns the number of the elements
extend() -> adds the elements at the end of the list
index() -> index of the value
insert() -> adds an element at the specified position
pop() -> removes the element at the specified position
remove() -> removes the item with the specified value
reverse() -> reverses the order of the list
sort() -> sorts the list'''
