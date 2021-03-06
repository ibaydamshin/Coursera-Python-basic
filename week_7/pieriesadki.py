""""
    На Новом проспекте для разгрузки было решено пустить два новых автобусных
    маршрута на разных участках проспекта. Известны конечные остановки каждого
    из автобусов. Определите количество остановок, на которых можно пересесть
    с одного автобуса на другой.

    Формат ввода
    Вводятся четыре числа, не превосходящие 100, задающие номера конечных
    остановок. Сначала для первого, потом второго автобуса
    (см. примеры).

    Формат вывода

    Ваша программа должна выводить одно число – искомое количество остановок.

    Примечания
                        |----- 1-й автобус -----|
        1-------2-------3-------4-------5-------6
                |- 2-й автобус -|

    Пояснения Первый пример: первый автобус ходит
    с 3-й остановки по 6-ю и обратно, а второй с 2-й по 4-ю и обратно.
    Пересесть с одного автобуса на другой можно на 3-й и 4-й остановках.
    Их две. Второй пример: автобусы не имеют общих остановок.

Примеры

Тест 1
Входные данные:
3 6 4 2

Вывод программы:
2


Тест 2
Входные данные:
3 1 5 10

Вывод программы:
0

"""

stops = list(map(int, input().split()))
bus1 = {i for i in range(min(stops[0:2]), max(stops[0:2]) + 1)}
bus2 = {i for i in range(min(stops[2:4]), max(stops[2:4]) + 1)}
print(len(bus1 & bus2))
