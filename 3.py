report = []
poor =[]
summa = 0
with open('test3.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    print("Сотрудники, имеющие оклад менее 20000:")
    for i in lines:
        i = i.split(' ')
        report.append([i[0], float(i[1])])
        if float(i[1]) <= 20000:
            print(i[0])
        summa += float(i[1])
print(f"\nСредняя величина дохода сотрудников: {summa / len(report)} руб.")

