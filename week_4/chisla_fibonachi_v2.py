"""
    Напишите функцию phib(n), которая по данному целому неотрицательному n
    возвращает n-e число Фибоначчи.
    В этой задаче нельзя использовать циклы - используйте рекурсию.

    Формат ввода
    Вводится удовлетворяющее условию задачи число.

    Формат вывода
    Выведите ответ на задачу.

    Примечание
    Обратите внимание на нумерацию чисел, показанную в примерах.

Примеры

Тест 1
Входные данные:
1

Вывод программы:
1


Тест 2
Входные данные:
2

Вывод программы:
1


Тест 3
Входные данные:
3

Вывод программы:
2

"""


def phib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return phib(n - 2) + phib(n - 1)


print(phib(int(input())))