# # dog.py
# class Dog:
#     """A simple attempt to mmodel a dog."""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(f"{self.name} is now sitting.")
    
#     def roll_over(self):
#         """Simulate a dog rolling over in response to a command."""
#         print(f"{self.name} rolled over!!!")

# my_dog = Dog("Monkey", 34)
# print(f"I have a dog named {my_dog.name}. \nHe is {my_dog.age} years old.")
# my_dog.sit()
# my_dog.roll_over()

# your_dog = Dog("Donkey", 43)
# print(f"You have a dog named {your_dog.name}. \nHe is {your_dog.age} years old.")
# your_dog.sit()
# your_dog.roll_over()



# ## T I Y :
# # 9-1. Restaurant:
# #restaurant.py
# class Restaurant:
    
#     def __init__(self, name, type):
#         """Initialize attributes."""
#         self.restaurant_name = name
#         self.cuisine_type = type

#     def describe_restaurant(self):
        
#         print(f"\nRestaurant name: {self.restaurant_name} \nCuisine Type: {self.cuisine_type}")

#     def open_restaurant(self):

#         print(f"{self.restaurant_name} is now open!!!")


# restaurant = Restaurant("Unga Bunga", "Bengali")
# print(f"\nInformation about a {restaurant.cuisine_type} cuisine restaurant called {restaurant.restaurant_name}....")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# # 9-2. Three Restaurants:
# restaurant_1 = Restaurant("Ching Chan Chu", "Chinese")
# restaurant_2 = Restaurant("Otashi Botashi", "Japanese")
# restaurant_3 = Restaurant("Annionghaseo", "Korean")

# restaurant_1.describe_restaurant()
# restaurant_2.describe_restaurant()
# restaurant_3.describe_restaurant()


# # 9-3. Users:
# class User:

#     def __init__(self, first_name, last_name, contact, mail):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.contact = contact
#         self.mail = mail

#     def describe_user(self):
#         print(f'''Name: {self.first_name} {self.last_name}
# Contact: {self.contact}
# Mail: {self.mail}''')
        
#     def greet_user(self):
#         print(f"Hi {self.last_name}, Hope you are fine.")


# person_1 = User("Sheikh", "Hasina", 8801134841, "hasina_seikh@gmail.com")
# person_1.describe_user()
# person_1.greet_user()



# # car.py
# class Car:
#     """A simple attempt to represt a car."""

#     def __init__(self, brand, model, year):
#         """Initialize attributes to describe a car."""
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         return f"{self.year} {self.brand} {self.model}"
    
#     def update_odometer(self, milage):
#         """
#         Set the odometer reading to the given value.
#         Reject the change if it tries to roll the odometer back.
#         """
#         if milage >= self.odometer_reading:
#             self.odometer_reading = milage
#         else:
#             print("You can't roll back an odometer!!!")

#     def increment_odometer(self, miles):
#         """
#         Add the given amount to the odometer reading.
#         Reject Negetive increments.
#         """
#         if miles >= 0:
#             self.odometer_reading += miles
#         else:
#             print("You can't enter negative increments and roll back an odometer!!!")
    
#     def read_odometer(self):
#         """Print a statement showing the car's milage."""
#         print(f"This car has {self.odometer_reading} milage in it.")
    
# my_new_car = Car("Farrari", "488 Pista", 2021)
# #my_new_car.odometer_reading = 24
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.update_odometer(56)
# my_new_car.read_odometer()
# my_new_car.update_odometer(66)
# my_new_car.read_odometer()
# my_new_car.update_odometer(20)
# my_new_car.read_odometer()

# my_old_car = Car("Audi", "R1", 2004)
# print(my_old_car.get_descriptive_name())
# my_old_car.update_odometer(20_345)
# my_old_car.increment_odometer(100)
# my_old_car.read_odometer()
# my_old_car.increment_odometer(-100)
# my_old_car.read_odometer()



# ##T I Y:
# #9-4. Number Served:
# #restaurant.py
# class Restaurant:
    
#     def __init__(self, name, type):
#         """Initialize attributes."""
#         self.restaurant_name = name
#         self.cuisine_type = type
#         self.number_served = 0

#     def describe_restaurant(self):
#         """Print the informations of the retaurants."""
#         print(f"\nRestaurant name: {self.restaurant_name} \nCuisine Type: {self.cuisine_type}")

#     def open_restaurant(self):
#         """Print an opennning message."""
#         print(f"{self.restaurant_name} is now open!!!")

#     def set_number_served(self, number):
#         """Set the new value of customers."""
#         self.number_served = number
    
#     def increment_number_served(self, num_of_customers):
#         """Update the number of customers served by the restaurants."""
#         self.number_served += num_of_customers

# restaurant = Restaurant("Unga Bunga", "Chinese")
# print(f"{restaurant.restaurant_name} served {restaurant.number_served} people today!")
# restaurant.set_number_served(45)
# print(f"{restaurant.restaurant_name} served {restaurant.number_served} people today!")
# restaurant.increment_number_served(12)
# print(f"{restaurant.restaurant_name} served {restaurant.number_served} people today!")


# #9-5. Login Attempts:
# #user.py
# class User:

#     def __init__(self, first_name, last_name, contact, mail):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.contact = contact
#         self.mail = mail
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f'''Name: {self.first_name} {self.last_name}
# Contact: {self.contact}
# Mail: {self.mail}''')
        
#     def greet_user(self):
#         print(f"Hi {self.last_name}, Hope you are fine.")

#     def increment_login_attempts(self):
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         self.login_attempts = 0


# person_1 = User("Sheikh", "Hasina", 8801134841, "hasina_seikh@gmail.com")
# person_1.describe_user()
# person_1.greet_user()
# person_1.increment_login_attempts()
# print(f"{person_1.last_name}, you have attempted {person_1.login_attempts} times to login.")
# person_1.increment_login_attempts()
# print(f"{person_1.last_name}, you have attempted {person_1.login_attempts} times to login.")
# person_1.increment_login_attempts()
# print(f"{person_1.last_name}, you have attempted {person_1.login_attempts} times to login.")
# person_1.increment_login_attempts()
# print(f"{person_1.last_name}, you have attempted {person_1.login_attempts} times to login.")
# person_1.reset_login_attempts()
# print(f"{person_1.last_name}, you have attempted {person_1.login_attempts} times to login.")



## Inheritance:
## electric_car.py
class Car:
    """A simple attempt to represt a car."""

    def __init__(self, brand, model, year):
        """Initialize attributes to describe a car."""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.brand} {self.model}"
    
    def update_odometer(self, milage):
        """
        Set the odometer reading to the given value.
        Reject the change if it tries to roll the odometer back.
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!!!")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        Reject Negetive increments.
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't enter negative increments and roll back an odometer!!!")
    
    def read_odometer(self):
        """Print a statement showing the car's milage."""
        print(f"This car has {self.odometer_reading} milage in it.")


class ElectricCar(Car):
    """Reoresents aspects of a specific car, specific to electric vehicles."""

    def __init__(self, brand, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(brand, model, year)
        self.battery = Battery()


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} KMH battery.")


car = ElectricCar("Audi", "R8", 2014)
print(car.get_descriptive_name())
car.battery.describe_battery()