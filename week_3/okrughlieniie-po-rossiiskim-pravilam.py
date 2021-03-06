import math
"""
    По российский правилам числа округляются до ближайшего целого числа,
    а если дробная часть числа равна 0.5, то число округляется вверх.
    Дано неотрицательное число x, округлите его по этим правилам.
    Обратите внимание, что функция round не годится для этой задачи!

    Формат ввода
    Вводится неотрицательное число.
"""

n = float(input())

fractional = int(round(n % 1, 10) * 10)

if fractional >= 5:
    n = math.ceil(n)
else:
    n = math.floor(n)

print(n)
