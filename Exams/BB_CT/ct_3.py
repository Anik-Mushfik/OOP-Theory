# Qustion - 1:
class Vehical:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Vehical:", self.name)

class Car(Vehical):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def display(self):
        super().display()
        print("Color:", self.color)

my_car = Car("Toyota", "Lil")
my_car.display()


# Qustion - 2:
class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 0
    def __str__(self):
        return f"x={self.x} y={self.y}"
    
b = B()
print(b)


# Qustion - 3:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector((self.x + other.x), (self.y + other.y))
    def __mul__(self,other):
        return Vector((self.x * other), (self.y * other))
v1 = Vector(2, 3)
v2 = Vector(1, 2)
result = v1 + v2 * 2
print(result.x, result.y)


class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        self.y = 0
    def __str__(self):
        return f"x={self.x} y={self.y}"
    
b = B()
print(b)