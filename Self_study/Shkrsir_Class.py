# ## Shallow Copy:
# class A:
#     pass

# a= A()
# a.name = "UIU"
# print(a.name)
# b=a
# print(b.name)
# b.name = "United"
# print(a.name)
# print(b.name)

# ## Deep Copy:
# import copy
# class A:
#     pass
# a= A()
# a.name = "UIU"
# b= copy.deepcopy(a)
# print(b.name)
# b.name = "United"
# print(a.name)
# print(b.name)

# Prac - 1:
"""
Consider a game where we have multiple players. A player could be
modeled by a Player class with instance variables for name, points,
health, location, and so on. Each player would have the same
capabilities, but the methods could work differently based on the
different values in the instance variables.
"""
class Player:
    """A model of a player."""
    def __init__(self, name, points, health, location, balance):
        self.name = name
        self.points = points
        self.health = health
        self.location = location
    
    def




# Prac - 2:
"""
Imagine an address book. We could create a Person class with
instance variables for name, address, phoneNumber, and birthday. We
could create as many objects from the Person class as we want, one
for each person we know. The instance variables in each Person
object would contain different values. We could then write code to
search through all the Person objects and retrieve information about
the one or ones we are looking for.
"""
