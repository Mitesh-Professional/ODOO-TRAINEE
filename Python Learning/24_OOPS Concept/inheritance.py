# Single Inheritance
class Name:
    def __init__(self, name):
        self.name = name


class User(Name):
    def __init__(self, name):
        super().__init__(name)
        print("I am Single Inheritance:- ", name)


my_name = User("Mitesh")


# Multilevel Inheritance

class User1:
    def __init__(self, first_pin):
        self.first_pin = first_pin + "!"


class User2(User1):
    def __init__(self, first_pin, second_pin):
        super().__init__(first_pin)
        self.second_pin = second_pin + "/"


class User3(User2):
    def __init__(self, first_pin, second_pin, third_pin):
        super().__init__(first_pin, second_pin)
        self.third_pin = third_pin + "{}"
        print(f"I Am MultiLevel Inheritance:- {first_pin} {second_pin} {third_pin}")


users_pin = User3("first_pin", "second_Pin", "third_pin")


# Multiple inheritance
class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model


class Engine(Car):
    def __init__(self, name, model, engine_name):
        super().__init__(name, model)
        self.engine_name = engine_name
        print("I am Multiple Inheritance.")
        print(f"Car Name is {name}. and car model {model}. which engine have this car {engine_name}")


class Fuel(Car):
    def __init__(self,name,model,type_of_fuel):
        super().__init__(name, model)
        self.type_of_fuel = type_of_fuel
        print("I am Multiple Inheritance.")
        print(f"Car Name is {name}. and car model {model}. which fuel have this car {type_of_fuel}")


fuel_name = Fuel("Supera", "Toyota","Petrol")