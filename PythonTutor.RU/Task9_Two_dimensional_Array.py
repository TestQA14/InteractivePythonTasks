# -*- coding: utf-8 -*-

# Задача «Максимум»
"""
Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца,
в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот,
у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.
Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой.
"""

n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
curr_max = a[0][0]
best_i, best_j = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            best_i, best_j = i, j
print(best_i, best_j)

# Задача «Снежинка»
"""
Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент 
массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива, средний столбец 
массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать изображение 
звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами.
"""

n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[i][i] = '*'
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][n - i - 1] = '*'
for row in a:
    print(' '.join(row))

# Задача «Шахматная доска»
"""
Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" 
в шахматном порядке. В левом верхнем углу должна стоять точка.
"""

n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))

# Задача «Диагонали, параллельные главной»
"""
Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали должны 
быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, 
и т.д.
"""
#
"""

"""