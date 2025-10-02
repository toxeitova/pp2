#1 задача
class Text():
    def __init__(self):
        self.s = ""   #переменная для хранения строки

    def getString(self):
        self.s = input("Введите строку: ")

    def printString(self):
        print(self.s.upper())

s = Text()
s.getString()
s.printString()

#2 задача
class Shape:
    def __init__(self):
        pass   
    def area(self):
        return 0   
class Square(Shape):
    def __init__(self, length):
        self.length = length  
    def area(self):
        return self.length * self.length  
s = Shape()
print("Shape area:", s.area())   # 0
sq = Square(5)
print("Square area:", sq.area()) # 25

#3 задача
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
s = Shape()
print("Shape area:", s.area())      # 0

sq = Square(5)
print("Square area:", sq.area())    # 25

r = Rectangle(4, 6)
print("Rectangle area:", r.area())  # 24

#4 задача
import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
p1 = Point(2, 3)
p2 = Point(5, 7)
p1.show()  # (2, 3)
p2.show()  # (5, 7)
print("Distance:", p1.dist(p2))  # 5.0
p1.move(10, 15)
p1.show()  # (10, 15)

#5 задача
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def __str__(self):
        return f"Account owner: {self.owner}\nBalance: {self.balance}"

acc = Account("Aruzhan", 100)   
print(acc)                      
acc.deposit(50)              
acc.deposit(200)                
acc.withdraw(100)               
acc.withdraw(500)             
print(acc)                    

#6 задача

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17]
primes = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", primes)



