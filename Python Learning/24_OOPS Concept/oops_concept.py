class First:
    x = 12


Obj = First()

print(Obj.x)


class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print(f"Your Name is {self.fname} {self.lname}")
        # why __init__ not have return type
        
value = Name("Mitesh", "Amin")
# print(value)
