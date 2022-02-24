def my_func():
    res = 0
    while True:
        li = input("Введите числа, разделенные пробелом,  или 'x' для выхода: ").split()
        for i in li:
            try:
                if i == "x":
                    print(f"Сумма составила: {res}")
                    return
                else:
                    res += float(i)
            except:
                print("Введите числа, разделенные пробелом, или 'x' для выхода:")
        print(f"Сумма составила: {res}")


my_func()
