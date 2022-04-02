class Cell:
    def __init__(self, amount):
        self.amount = amount
        if amount <= 0:
            print('Операция невозможна')

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        result = self.amount - other.amount
        if result > 0:
            return result
        else:
            print(f'Операция невозможна')

    def __mul__(self, other):
        return self.amount * other.amount

    def __floordiv__(self, other):
        return self.amount // other.amount

    def make_order(self, row):

        result = ''
        for i in range(int(self.amount / row)):
            result += '*' * row + '\n'
        result += '*' * (self.amount % row) + '\n'
        return result


cell_1 = Cell(25)
cell_2 = Cell(20)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)

print(cell_1.make_order(10))
print(cell_2.make_order(10))

