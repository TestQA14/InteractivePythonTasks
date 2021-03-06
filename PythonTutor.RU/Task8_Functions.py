# -*- coding: utf-8 -*-
import math

# Задача «Длина отрезка»
"""
Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), 
вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и 
выведите результат работы этой функции.
"""

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2)))

# Задача «Отрицательная степень»
"""
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).

Стандартной функцией возведения в степень пользоваться нельзя.
"""

a = float(input())
n = int(input())
res = 0


def power(a, n):
    res = a**n


print(pow(a, n))

# Задача «Большие буквы»
"""
Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает его же, 
меняя первую букву на большую.
Например, print(capitalize('word')) должно печатать слово Word.
На вход подаётся строка, состоящая из слов, разделённых одним пробелом. Слова состоят из маленьких латинских 
букв. Напечатайте исходную строку, сделав так, чтобы каждое слово начиналось с большой буквы. При этом используйте 
вашу функцию capitalize().
Напомним, что в Питоне есть функция ord(), которая по символу возвращает его код в таблице ASCII, и функция chr(), 
которая по коду символа возвращает сам символ. Например, ord('a') == 97, chr(97) == 'a'.
"""


def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]


source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))

# Задача «Возведение в степень»
"""
Дано действительное положительное число a и целое неотрицательное число n. Вычислите an не используя циклы, 
возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение an=a⋅an-1.
Решение оформите в виде функции power(a, n).
"""


def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


print(power(float(input()), int(input())))

# Задача «Разворот последовательности»
"""
Дана последовательность целых чисел, заканчивающаяся числом 0. Выведите эту последовательность в обратном 
порядке. При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных. 
Рекурсия вам поможет.
"""


def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)


reverse()

# Задача «Числа Фибоначчи»
"""
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. В этой 
задаче нельзя использовать циклы — используйте рекурсию.
"""


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(int(input())))

