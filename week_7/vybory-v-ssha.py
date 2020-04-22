"""
    Как известно, в США президент выбирается не прямым голосованием, а путем
    двухуровневого голосования. Сначала проводятся выборы в каждом штате и
    определяется победитель выборов в данном штате. Затем проводятся
    государственные выборы: на этих выборах каждый штат имеет определенное
    число голосов — число выборщиков от этого штата. На практике, все
    выборщики от штата голосуют в соответствии с результатами голосования
    внутри штата, то есть на заключительной стадии выборов в голосовании
    участвуют штаты, имеющие различное число голосов. Вам известно за кого
    проголосовал каждый штат и сколько голосов было отдано данным штатом.
    Подведите итоги выборов: для каждого из участника голосования определите
    число отданных за него голосов.

    Формат ввода
    Каждая строка входного файла содержит фамилию кандидата, за которого
    отдают голоса выборщики этого штата, затем через пробел идет количество
    выборщиков,отдавших голоса за этого кандидата.

    Формат вывода
    Выведите фамилии всех кандидатов в лексикографическом порядке, затем, через
    пробел, количество отданных за них голосов.

Примеры
Тест 1
Входные данные:
McCain 10
McCain 5
Obama 9
Obama 8
McCain 1

Вывод программы:
McCain 16
Obama 17



Тест 2
Входные данные:
ivanov 100
ivanov 500
ivanov 300
petr 70
tourist 1
tourist 2

Вывод программы:
ivanov 900
petr 70
tourist 3



Тест 3
Входные данные:
bur 1

Вывод программы:
bur 1

"""

fin = open('input.txt', 'r', encoding='utf-8')
candidates = {}
for line in fin:
    name, rate = line.split()
    candidates[name] = candidates.get(name, 0) + int(rate)

for person in sorted(candidates):
    print(person, candidates[person])

fin.close()
