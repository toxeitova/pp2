#1
def generate_squares(N):
    for i in range(1, N+1):
        yield i ** 2 
num = int(input("Enter a number N: "))
for square in generate_squares(num):
    print(square)

#2
def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
n = int(input("Enter a number: "))
print(", ".join(str(num) for num in even_numbers(n)))

#3
def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Enter a number: "))
print("Numbers divisible by both 3 and 4:")
for num in divisible_by_3_and_4(n):
    print(num)

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))
print(f"Squares of numbers from {a} to {b}:")
for square in squares(a, b):
    print(square)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number: "))
print(f"Countdown from {n} to 0:")

for num in countdown(n):
    print(num)

