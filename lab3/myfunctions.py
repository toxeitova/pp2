import math
from itertools import permutations

# 1. Перевод грамм 
def grams_to_ounces(grams):
    return 28.3495231 * grams

# 2. Фаренгейт to Цельсий
def fahrenheit_to_celsius(f):
    return (5 / 9) * (f - 32)

# 3. Объём сферы
def sphere_volume(r):
    return (4/3) * math.pi * (r ** 3)

# 4. Уникальные элементы списка
def unique_list(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

# 5. Палиндром
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# 6. Гистограмма
def histogram(lst):
    for num in lst:
        print("*" * num)

# 7. Простое число
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 8. Фильтр простых чисел
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# 9. Перестановки строки
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

# 10. Реверс слов в предложении
def reverse_sentence(s):
    words = s.split()
    return " ".join(words[::-1])

# 11. Проверка "33" рядом
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# 12. Проверка "007" в списке
def spy_game(nums):
    code = [0, 0, 7]
    idx = 0
    for n in nums:
        if n == code[idx]:
            idx += 1
            if idx == len(code):
                return True
    return False

# 13. Классическая задача (курицы и кролики)
def solve(numheads, numlegs):
    for r in range(numheads + 1):
        c = numheads - r
        if 2*c + 4*r == numlegs:
            return c, r
    return None, None

print("100 grams in ounces:", grams_to_ounces(100))
print("212°F in Celsius:", fahrenheit_to_celsius(212))
print("Volume of sphere radius 3:", sphere_volume(3))

print("Unique list:", unique_list([1,2,2,3,4,4,5]))
print("Is 'madam' palindrome?", is_palindrome("madam"))

print("Prime numbers:", filter_prime([1,2,3,4,5,6,7,8,9,10,11]))
print("Permutations of 'abc':", string_permutations("abc"))
print("Reverse sentence:", reverse_sentence("We are ready"))

print("Has 33?", has_33([1,3,3]))
print("Spy game:", spy_game([1,2,4,0,0,7,5]))
print("Solve heads=35, legs=94:", solve(35,94))
