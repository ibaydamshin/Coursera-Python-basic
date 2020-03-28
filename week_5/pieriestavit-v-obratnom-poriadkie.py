"""
    Переставьте элементы данного списка в обратном порядке, затем выведите
    элементы полученного списка. Эта задача отличается от предыдущей тем,
    что вам нужно изменить значения элементов самого списка,
    поменяв местами A[0] c A[n-1], A[1] с A[n-2],
    а затем вывести элементы списка подряд.

    Предлагается в учебных целях проделать это вручную, например,
    не используя срезов и стандартных функций.

    Формат ввода
    Вводится список чисел. Все числа списка находятся на одной строке.

"""


def revers_L(L):
    for i in range(len(L) // 2):
        L[i], L[-(i + 1)] = L[-(i + 1)], L[i]
    return L


lst = list(map(int, input().split()))
print(*revers_L(lst))