def my_f(a, b):
    try:
        res = a/b
        return res
    except ZeroDivisionError:
        return "На ноль делить нельзя!"


print(my_f(int(input("Введите число a = ")), int(input("Введите число b = "))))

