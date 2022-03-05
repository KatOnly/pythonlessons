from functools import reduce


def prod(a, b):
    return a * b


print(reduce(prod, [i for i in range(100, 1001) if i % 2 == 0]))


