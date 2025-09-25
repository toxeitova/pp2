#Python arithmetic operators
x = 8
y = 4
print(x+y) #addition
print(x-y) #substraction
print(x*y) #multiplication
print(x/y) #division 2.0
print(x%y) #modulus 0
print(x**y) #exponentiation 
print(x//y) #floor division  2

#Python assignment operators

x = 8
print(x)

x = 8
x+=2
print(x)

x = 8
x-=3
print(x)

x = 8
y = 4
z = 15
n = 2
x*=9
y/=3
z%=3
n**=2
print(x)
print(y)
print(z)
print(n)

#& — это такой оператор, который сравнивает два числа по их двоичным “лампочкам” (битам). там где 1 оставляет 1, в остальных 0. тут как умножение
x = 5 #101
x &= 3 #011
print(x) #001 -> 1

#это побитовое ИЛИ, как сложение работает
x = 5 #101
x |= 3 #011
print(x) #111 -> 7

#XOR , если биты одинаковые то ставится 0. если разные, то 1
x = 5 #101
x ^= 3 #011
print(x) #110 -> 2^0 * 0 + 2^1 * 1 + 2^2 * 1 = 0 + 2 + 4 = 6 

x = 5 #делим число на 2        
x >>= 3 #три раза. 5//2=2  2//2=1 1//2=0.   >>n -> делим на 2^n
print(x) #0   

x = 5 
x <<= 3 #<<n -> умножаем на 2^n  5*2^3 = 40
print(x)

print(x := 3) #моржовый оператор - присваиваем значение переменной и возвращаем. x = 3

#logical operators
x = 5
print(not(x > 3 and x < 10)) 

x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 4)

#comparison operators
x = 5
y = 3
z = 7
u = 8
o = 8
t = 60
print(x >= y)
print(z < u)
print(u <= o)


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y) #returns True because x is equal to y


x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]
print("pineapple" not in x) 












