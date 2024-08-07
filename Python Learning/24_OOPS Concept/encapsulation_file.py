# Encapsulation

class Name:
    def __init__(self, full_name, company):
        self.__full_name = full_name
        self.__company = company

    def get_name(self):
        return f"My Name is {self.__full_name}. My office name is {self.__company}."


class Print(Name):
    def __init__(self, full_name, company):
        super().__init__(full_name, company)
        # print(")


my_name = Print("Mitesh", "google")
print(my_name.get_name())
