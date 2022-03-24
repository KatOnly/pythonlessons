with open('test5.txt', 'w+') as f:
    line = input('Введите числа, разделяя пробелом: \n')
    f.writelines(line)
    digit = line.split()
    print(sum(map(float, digit)))
