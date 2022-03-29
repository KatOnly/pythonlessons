class Car:
    def __init__(self, name, color, speed, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.sp = is_police

    def go(self):
        print(f"{self.name} {self.color} цвета начинает движение")

    def stop(self):
        print("Остановка")

    def turn(self, direction):
        print(f"Поворот  {direction}")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")

    def is_police(self):
        if self.sp == "True":
            print("Полицейская машина\n")
        else:
            print()


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Вы превысили скорость")
        else:
            print(f"Текущая скорость {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed >= 40:
            print("Вы превысили скорость")
        else:
            print(f"Текущая скорость {self.speed}")


class PoliceCar(Car):
    pass


work1 = WorkCar("Mazda", "голубого", 40, "False")
work1.go()
work1.turn("направо")
work1.stop()
work1.show_speed()
work1.is_police()

town1 = TownCar("Toyota", "красного", 100, "False")
town1.go()
town1.turn("налево")
town1.show_speed()
town1.stop()
town1.is_police()

sport1 =SportCar("Lamborghini", "желтого", 250, "False")
sport1.go()
sport1.turn("налево")
sport1.show_speed()
sport1.stop()
sport1.is_police()

police1 = PoliceCar("Ford", "белого", 80, "True")
police1.go()
police1.turn("налево")
police1.turn("направо")
police1.show_speed()
police1.stop()
police1.is_police()

