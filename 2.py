
class Road:
    def __init__(self, length, width):
        self._lth = length
        self._w = width
        self.weight = 25
        self.dimension = 5

    def asphalt(self):
        asphalt = self._lth*self._w*self.weight*self.dimension/1000
        print(f"Масса асфальта, необходимого для покрытия всей дороги, составляет {(asphalt)} т")


m = Road(5000, 20)
m.asphalt()
