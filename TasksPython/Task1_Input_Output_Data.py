# -*- coding: utf-8 -*-
# Задача «Сумма трёх чисел»
""" Напишите программу, которая считывает три числа и выводит их сумму.
Каждое число записано в отдельной строке. """

a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

# Задача «Площадь прямоугольного треугольника»
""" Напишите программу, которая считывает длины двух катетов 
в прямоугольном треугольнике и выводит его площадь. Каждое число записано в отдельной строке."""

b = int(input())
h = int(input())
print(0.5 * b * h)

# Задача «Дележ яблок»
""" n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. 
Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке? 
Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа). """

n = int(input())
k = int(input())
print(k // n, k % n)

# Задача «Электронные часы»
""" Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать
 электронные часы в этот момент. Программа должна вывести два числа: количество часов (от 0 до 23) 
 и количество минут (от 0 до 59). Учтите, что число n может быть больше, чем количество минут в сутках. """

n = int(input())
if n < 1440:
    h = n // 60
    m = n % 60
elif n >= 1440:
    h = (n // 60) - 24
    m = n % 60
if h > 23:
    while h > 23:
        h = h - 24
if m > 59:
    m = m//60
print(h)
print(m)

# Задача «Hello, Harry!»
"""Напишите программу, которая приветствует пользователя, выводя слово Hello, введенное имя и знаки 
препинания по образцу:"""

name = input("What is your name? ")
print("Hello," + " " + name + "!")

# Задача «Следующее и предыдущее»
""" Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в 
примере (пробелы важны!). """

number = int(input())
next = number + 1
previous = number -1
print("The next number for the number " + str(number) + " is " + str(next) + "." + "\n" +
"The previous number for the number " + str(number) + " is " + str(previous) + ".")

# Задача «Парты»
""" В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят 
в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты. 
За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов. 
Сколько всего нужно закупить парт чтобы их хватило на всех учеников? 
Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов. """

c1 = int(input())
c2 = int(input())
c3 = int(input())
if c1 % 2 > 0:
    c1 = (c1//2) + 1
else:
    c1 = c1//2
if c2 % 2 > 0:
    c2 = (c2//2) + 1
else:
    c2 = c2//2
if c3 % 2 > 0:
    c3 = (c3//2) + 1
else:
    c3 = c3//2
print(c1 + c2 + c3)
