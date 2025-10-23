#1

numbers = [1, 2, 3, 4, 5]
result = eval('*'.join(map(str, numbers)))
print("Result:", result)

nums = [8, 8, 8, 8]
z = 1
for i in range(len(nums)):
    z = z * nums[i]
print(z)


#2
text = input("Enter a string: ")
upper = 0
lower = 0
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)

#3
text = input("Enter a string: ")
text = text.replace(" ", "").lower()
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

#4
import time
import math
num = int(input())
ms = int(input())
time.sleep(ms / 1000)
print("Square root of", num, "after", ms, "milliseconds is", math.sqrt(num))

#5
mytuple = (1, True, True)
x = all(mytuple)
print(x)


