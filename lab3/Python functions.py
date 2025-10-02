#1 
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
print(grams_to_ounces(100))   
print(grams_to_ounces(1))     

#2
def fahrenheit_to_celsius(f):
    c = (5 / 9) * (f - 32)
    return c
f = float(input("Enter temperature in Fahrenheit: "))
c = fahrenheit_to_celsius(f)
print(c)   

#3
def solve(numheads, numlegs):
    for r in range(numheads + 1):   
        c = numheads - r           
        if 2*c + 4*r == numlegs: 
            return c, r
    return None, None  
chickens, rabbits = solve(35, 94)
print("Chickens:", chickens)
print("Rabbits:", rabbits)

#4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Prime numbers:", filter_prime(nums))

#5
from itertools import permutations
def print_permutations():
    s = input("Enter a string: ")
    perms = permutations(s)   
    for p in perms:
        print("".join(p))
print_permutations()

#6
def reverse_sentence():
    s = input("Enter a sentence: ")
    words = s.split()          
    reversed_words = words[::-1]  
    return " ".join(reversed_words)
print(reverse_sentence())

#7
def has_33(nums):
    for i in range(len(nums) - 1):     # идём до предпоследнего элемента
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))      # True
print(has_33([1, 3, 1, 3]))   # False
print(has_33([3, 1, 3]))      # False

#8
def spy_game(nums):
    code = [0, 0, 7]  
    idx = 0            
    for n in nums:
        if n == code[idx]:
            idx += 1
            if idx == len(code):   # нашли всю последовательность
                return True
    return False
print(spy_game([1,2,4,0,0,7,5]))  # True
print(spy_game([1,0,2,4,0,5,7]))  # True
print(spy_game([1,7,2,0,4,5,0]))  # False

#9
import math
def sphere_volume(r):
    return (4/3) * math.pi * (r ** 3)
print(sphere_volume(1))  
print(sphere_volume(3))  

#10
def unique_list(lst):
    new_list = []
    for item in lst:
        if item not in new_list:   # добавляем только если элемента ещё нет
            new_list.append(item)
    return new_list
print(unique_list([1, 2, 2, 3, 4, 4, 5]))   # [1, 2, 3, 4, 5]
print(unique_list(["a", "b", "a", "c", "b"])) # ['a', 'b', 'c']

#11
def is_palindrome(s):
    # убираем пробелы и приводим к нижнему регистру
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome("madam"))       # True
print(is_palindrome("hello"))       # False
print(is_palindrome("A man a plan a canal Panama"))  # True

#12
def histogram(lst):
    for num in lst:
        print("*" * num)
histogram([4, 9, 7])

#13
import random
def guess_game():
    print("Hello! What is your name?")
    name = input()

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)   # случайное число от 1 до 20
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())        # пользователь вводит число
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
guess_game()

#14 в другом файле отдельно 
