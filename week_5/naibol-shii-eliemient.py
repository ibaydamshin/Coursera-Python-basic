"""
    Дан список чисел. Выведите значение наибольшего элемента в списке, а затем
    индекс этого элемента в списке. Если наибольших элементов несколько,
    выведите их значение и индекс первого из них.
    Формат ввода

    Вводится список чисел. Все числа списка находятся на одной строке.

"""


def maxelm(L):
    v, k = L[0], 0
    for i in range(len(L)):
        if v < L[i]:
            v, k = L[i], i
        i += 1
    return v, k


lst = list(map(int, input().split()))
print(*maxelm(lst))
