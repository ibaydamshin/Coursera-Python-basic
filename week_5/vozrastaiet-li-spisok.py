"""
    Дан список. Определите, является ли он монотонно возрастающим
    (то есть верно ли, что каждый элемент этого списка больше предыдущего).
    Выведите YES, если массив монотонно возрастает и NO в противном случае.
    Решение оформите в виде функции IsAscending(A).
    В данной функции должен быть один цикл while, не содержащий вложенных
    условий и циклов — используйте схему линейного поиска.

"""


def is_ascending(A):
    i = 1
    IsNo = False
    IsYes = True
    while i < len(A) and IsYes:
        IsYes = A[i] > A[i - 1]
        IsNo = A[i] <= A[i - 1]
        i += 1
    return 'YES' * IsYes + 'NO' * IsNo


lst = list(map(int, input().split()))
print(is_ascending(lst))
