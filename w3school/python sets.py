#sets - unordered, no duplicates, mutable(like LIST)
numbers = {1, 1, 3, 4, 5}
print(numbers)
print(type(numbers))

thisset = {"apple", "banana", "cherry", True, 1, 2} #false and 0 are the same
print(thisset) #dont allow duplicate values

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))

#set constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Access
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Check if "banana" is present in the set
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Check if "banana" is NOT present in the set
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

#add
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

#add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#remove
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#remove "banana" by using the discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#remove a random item by using the pop() method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#the clear() method empties the set
hisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#the clear() method empties the set
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#LOOP SET
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#join

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

