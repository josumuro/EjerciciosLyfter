class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"Brand: {self._brand}, Year: {self._year}"


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self._doors = doors

    def get_info(self):
        return f"{super().get_info()}, Doors: {self._doors}"


class Motorcycle(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self._type = type

    def get_info(self):
        return f"{super().get_info()}, Type: {self._type}"


my_car = Car("Toyota", 2020, 4)
my_moto = Motorcycle("Honda", 2022, "Sport")

print(my_car.get_info())
print(my_moto.get_info())