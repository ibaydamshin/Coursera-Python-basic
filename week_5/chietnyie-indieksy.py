"""
    Выведите все элементы списка с четными индексами
    (то есть A[0], A[2], A[4], ...).
    Программа должна быть эффективной и не выполнять лишних действий!

    Формат ввода
    Вводится список чисел. Все числа списка находятся на одной строке.

"""

lst = list(map(int, input().split()))
print(' '.join(map(str, lst[::2])))
