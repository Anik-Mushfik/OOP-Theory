# dog.py
class Dog:
    """A simple attempt to mmodel a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!!!")

my_dog = Dog("Monkey", 34)
print(f"I have a dog named {my_dog.name}. \nHe is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("Donkey", 43)
print(f"You have a dog named {your_dog.name}. \nHe is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()


## T I Y :
# 9-1. Restaurant:
class Restaurant:
    
    def __init__(self, name, type):
        """Initialize attributes."""
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        
        print(f"Restaurant name: {self.restaurant_name} \nCuisine Type: {self.cuisine_type}")

    def open_restaurant(self):

        print(f"{self.restaurant_name} is now open!!!")


restaurant = Restaurant("Unga Bunga", "Bengali")
print(f"\nInformation about a {restaurant.cuisine_type} cuisine restaurant called {restaurant.restaurant_name}....\n")
restaurant.describe_restaurant()
restaurant.open_restaurant()