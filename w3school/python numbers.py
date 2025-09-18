x = 8
y = 0.5
z = 1j
print(type(x))
print(type(y))
print(type(z))

#int
x = 4
y = 43753584583
z = -54783945934
print(type(x))
print(type(y))
print(type(z))

#float
x = 7.80
y = 5.2
z = -25.00
print(type(x))
print(type(y))
print(type(z))

#float
x = 490e8
y = 18E5
z = -99.8e300
print(type(x))
print(type(y))
print(type(z))

#complex
x = 6+8j
y = 8j
z = -8j
print(type(x))
print(type(y))
print(type(z))

#convert to another type
x = float(5)
y = int(0.5)
z = complex(1)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

#random
import random
print(random.randrange(1, 100))
