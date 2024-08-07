class Car:
    def __init__(self, name):
        self.__name = name
    @property
    def name(self):
        return self.__name

Tata = Car("Safari")
# print(Tata.name_print())
# Tata.name = "nexon"
print(Tata.name)

