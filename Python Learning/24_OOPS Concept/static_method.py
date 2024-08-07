class Car:
    how_many_car = 0

    def __init__(self, name):
        self.name = name
        Car.how_many_car += 1
    @staticmethod
    def descriptions():
        return "This Function created By Mitesh."

Tata = Car("Safari")
print(Tata.name)
Tata = Car("Nexon")
print(Tata.name)
print(Car.how_many_car)
print("This is StaticMethod Example:- ")
print(Car.descriptions())