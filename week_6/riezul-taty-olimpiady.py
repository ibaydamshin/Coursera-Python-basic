"""
    В олимпиаде участвовало N человек. Каждый получил определенное количество
    баллов, при этом оказалось, что у всех участников разное число баллов.
    Упорядочите список участников олимпиады в порядке убывания набранных
    баллов.

    Формат ввода
    Программа получает на вход число участников олимпиады N.
    Далее идет N строк, в каждой строке записана фамилия участника, затем,
    через пробел, набранное им количество баллов.

    Формат вывода
    Выведите список участников (только фамилии) в порядке убывания набранных
    баллов.

    Примеры
    Тест 1
    Входные данные:
    3
    Ivanov 15
    Petrov 10
    Sidorov 20

    Вывод программы:
    Sidorov
    Ivanov
    Petrov

"""

students_list = []
j = int(input())
for i in range(j):
    n, s, = input().split()
    students_list.append((int(s), n))

students_list.sort(reverse=True)

for i in students_list:
    print(i[1])
