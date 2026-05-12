class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} ha subido al bus.")
        else:
            print("El bus está lleno. No se pueden agregar más pasajeros.")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} ha bajado del bus.")
        else:
            print(f"{person.name} no está en el bus.")

class Person:
    def __init__(self, name):
        self.name = name
bus = Bus(max_passengers=2)
person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person("Charlie")
bus.add_passenger(person1) 
bus.add_passenger(person2)
bus.add_passenger(person3)
bus.remove_passenger(person1)
