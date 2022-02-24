def my_func(a, b, c):                                         # 1 вариант
    if a < b and a < c:
        return b + c
    if b < a and b < c:
        return a + c
    if c < a and c < b:
        return b + a


print(my_func(int(input("a=")), int(input("b=")), int(input("c="))))       # как правильно оформить, чтобы ввывод данных был в формате "Сумма наибольших двух аргументов: "


def my_func(a, b, c):                                      # 2 вариант
    print((a + b + c) - min(a, b, c))


my_func(int(input("a=")), int(input("b=")), int(input("c=")))
