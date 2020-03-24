"""
    Даны два четырёхзначных числа A и B. Выведите все четырёхзначные числа на
    отрезке от A до B, запись которых является палиндромом.

    Формат ввода
    Вводятся два целых числа A и B

Пример:
Тест 1
Входные данные:
1600
2100

Вывод программы:
1661
1771
1881
1991
2002

"""

for i in range(int(input()), int(input()) + 1):
    t = tuple(str(i))
    if t[0] == t[3] and t[1] == t[2]:
        print(i)