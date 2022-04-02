class Matrix:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        for row in self.a:
            for i in row:
                print(f"{i:3}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.a)):
            for j in range(len(other.a[i])):
                self.a[i][j] = self.a[i][j] + other.a[i][j]
        result = self.a
        return Matrix(result)


m1 = Matrix([[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]])
m2 = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2], [2, 2, -7]])
print(m1)
print(m2)
print(m1 + m2)
