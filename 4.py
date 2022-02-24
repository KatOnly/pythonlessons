def my_func(x, y):
    res = x ** y
    print(res)


my_func(float(input("Введите положительное число: ")), int(input("Введите отрицательное число: ")))


def my_func_2(x, y):
    n = y - 1
    res = 1 / x
    while n < abs(y):
        res = res * (1 / x)
        n += 1
    return res


my_func(float(input("Введите положительное число: ")), int(input("Введите отрицательное число: ")))

