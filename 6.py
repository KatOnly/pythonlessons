from itertools import count, cycle


def count_func(first):
    print("Итератор, генерирующий целые числа, начиная с указанного:")
    for el in count(first):
        if el > 20:
            break
        else:
            print(el)


count_func(first=int(input("Введите первое число: ")))

print("Итератор, повторяющий элементы некоторого списка, определенного заранее:")
i = 0
for el in cycle([1, 20, 3]):
    if i > 10:
        break
    print(el)
    i += 1

