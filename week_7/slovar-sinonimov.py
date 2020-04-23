"""
    Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к
    парному ему слову. Все слова в словаре различны. Для одного данного слова
    определите его синоним.

    Формат ввода
    Программа получает на вход количество пар синонимов N. Далее следует N
    строк, каждая строка содержит ровно два слова-синонима. После этого
    следует одно слово.

    Формат вывода
    Программа должна вывести синоним к данному слову.

    Примечания
    Эту задачу можно решить и без словарей (сохранив все входные данные в
    списке), но решение со словарем будет более простым.


Примеры
Тест 1
Входные данные:
3
Hello Hi
Bye Goodbye
List Array
Goodbye

Вывод программы:
Bye


Тест 2
Входные данные:
1
beep Car
Car

Вывод программы:
beep


Тест 3
Входные данные:
2
Ololo Ololo
Numbers 1234567890
Numbers

Вывод программы:
1234567890

"""

fin = open('input.txt', 'r', encoding='utf-8')
synonym = {}
for i in range(int(fin.readline().strip())):
    v, k = fin.readline().strip().split()
    synonym[k] = v
    synonym[v] = k

fin.close()
print(synonym[fin.readline().strip()])