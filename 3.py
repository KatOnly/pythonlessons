class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"{self.surname},{self.name}")

    def get_total_income(self):
        print(f"{sum(self._income.values())}")


p = Position('Иван', 'Иванов', 'слесарь', '12000', '1500')
p.get_full_name()
p.get_total_income()
