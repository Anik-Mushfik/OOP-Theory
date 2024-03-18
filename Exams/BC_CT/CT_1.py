# Qustion no -2:(Output Tracing)
class Room:
    def __init__(self, name, height, width):
        self.name = name
        self.height = height
        self.width = width

    def __str__(self):
        return f"{self.name} Room, Area: {self.getarea()} sqft"
    
    def getarea(self):
        return self.height * self.width
    
class House:
    def __init__(self, name, r1, r2):
        self.name = name
        self.room1 = r1
        self.room2 = r2

    def describe(self):
        print(f"This is {self.name} Bari and it has {self.room1}")
        print(f"It also has {self.room2}")


msbed = Room("Master Bed", 12, 10)
kitchen = Room("Kitchen", 9, 7)
house = House("Jomidar", msbed, kitchen)
house.describe()
