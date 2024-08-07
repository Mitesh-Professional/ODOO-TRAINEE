class A:
    def __init__(self):
        print("I Am Class A.")

    def sum(self, a, b):
        self.a = a
        self.b = b
        return a + b


class B(A):
    def __init__(self):
        # super().__init__()
        print("I Am Class B.")

    def sum(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        return a + b + c


class_a = A()
class_b = B()

print(class_a.sum(10,20))
print(class_b.sum(10,20,20))

print("This is a Overloading!")
