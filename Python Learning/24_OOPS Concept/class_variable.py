class Car:
    how_many_car = 0

    def __init__(self, name):
        self.name = name
        Car.how_many_car += 1

Tata = Car("Safari")
print(Tata.name)
Tata = Car("Nexon")
print(Tata.name)
print(Car.how_many_car)