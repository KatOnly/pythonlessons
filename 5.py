class Stationery:
    def __init__(self, title):
        self.t = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем {self.t}")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем {self.t}")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Рисуем {self.t}")


pen1 = Pen("ручкой")
pen1.draw()

pencil1 = Pencil("карандашом")
pencil1.draw()

handle1 = Handle("маркером")
handle1.draw()
