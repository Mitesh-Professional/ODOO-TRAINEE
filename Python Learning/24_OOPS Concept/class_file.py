class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        print(f"Car Full Name of a {self.model}. and company is a {self.brand}.")


my_car = Car("toyota", "supera")
my_car.full_name()
