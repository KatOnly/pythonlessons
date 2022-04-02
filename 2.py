from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.size = size
        super().__init__(name)

    @property
    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 1)


class Suit(Clothes):
    def __init__(self, name, height):
        self.height = height
        super().__init__(name)

    @property
    def fabric_consumption(self):
        return round(2 * self.height + 0.3, 1)


coat = Coat('Пальто', 52)
suit = Suit('Костюм', 62)
print(f'Для пошива пальто нужно: {coat.fabric_consumption} метров ткани')
print(f'Для пошива костюма нужно: {suit.fabric_consumption} метров ткани')
print(f'Суммарный расход ткани: {coat.fabric_consumption + suit.fabric_consumption}')
