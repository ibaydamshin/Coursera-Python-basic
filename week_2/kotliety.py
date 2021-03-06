"""
На сковородку одновременно можно положить k котлет.
Каждую котлету нужно с каждой стороны обжаривать m минут непрерывно.
За какое наименьшее время удастся поджарить с обеих сторон n котлет?
Формат ввода
Программа получает на вход три числа: k,m,n.
Формат вывода
Программа должна вывести одно число: наименьшее количество минут.
"""
k, m, n = int(input()), int(input()), int(input())
# k, m, n = 10, 1, 16

if n == 0:
    answer = 0
elif n < k:
    answer = 2 * m
elif n % k == 0:
    answer = (n // k) * 2 * m
elif n % k > k // 2:
    answer = (n // k) * 2 * m + 2 * m
else:
    answer = (n // k) * 2 * m + m

print(answer)
