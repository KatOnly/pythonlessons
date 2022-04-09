class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, Equipment):
        self._dict.setdefault(Equipment.group_name(), []).append(Equipment)

    # def extract(self, name):
    #     if not self._dict[name]:
    #         self._dict.setdefault(name).pop(0)

    @property
    def dict(self):
        return self._dict


class Equipment:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price
        self.group = self.__class__.__name__
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Год выпуска': self.year, 'Цена за ед': self.price}

    @property
    def reception(self):
        try:
            name = input(f'Введите наименование ')
            year = int(input(f'Введите год выпуска '))
            price = int(input(f'Введите цену за единицу '))
            unique = {'Модель устройства': name, 'Год выпуска': year, 'Цена за ед': price}
            self.my_store.append(unique)

        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.extend(self.my_store)              # почему  выводятся только последние введенные данные,
            print(f'Весь склад -\n {self.my_store_full}')

        else:
            return Equipment.reception

    def group_name(self):
        return f"{self.group}"

    def __repr__(self):
        return f"{self.name} {self.year} {self.price} "


class Printer(Equipment):
    def __init__(self, name, year, price):
        super().__init__(name, year, price)

    def action(self):
        return f"Print"


class Scaner(Equipment):
    def __init__(self, name, year, price):
        super().__init__(name, year, price)

    def action(self):
        return f"Scan"


class Xerox(Equipment):
    def __init__(self, name, year, price):
        super().__init__(name, year, price)

    def action(self):
        return f"Copy"


sklad = Sklad()
scaner = Scaner('hp', '30000', 1997)
sklad.add_to(scaner)
printer = Printer("brother", "20000", 2000)
sklad.add_to(printer)
xerox = Xerox("Canon", "45000", 2020)
sklad.add_to(xerox)

print(scaner.reception)
print(scaner.action())
print(printer.reception)
print(printer.action())
print(xerox.reception)
print(xerox.action())


print(sklad._dict)


