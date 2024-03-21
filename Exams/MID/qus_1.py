# (a)-
class Account:
    unique_ID = 1000
    def __init__(self, user_name):
        self.trasactions = []
        self.user_name = user_name
        self.balance = 500

    def withdraw(self):
        pass



# # (b)-
# from abc import ABC, abstractmethod
# import copy


# class Ride(ABC):
#     def __init__(self, base_fare, per_km_fare):
#         self.base_fare = base_fare
#         self.per_km_fare = per_km_fare

#     def calculateFare(self, distance, greeting):
#         greeting()
#         return self.base_fare + (self.per_km_fare * distance)
    

# class Car(Ride):
#     def __init__(self, base_fare, per_km_fare):
#         super().__init__(base_fare, per_km_fare)

#     def calculateFare(self, distance, greeting):
#         total_fare = super().calculateFare(distance, greeting)

#         if (distance > 10):
#             return total_fare * 0.9
#         else:
#             return total_fare
        

# def welcomeUser():
#     print("Welcome to Uthao")
#     print("Here is your fare breakdown!!!")


# variable = welcomeUser
# car1 = Car(40, 15)
# car1_copy = car1
# car1_copy.base_fare = 45

# car2 = Car(50, 20)
# car2_copy = copy.deepcopy(car2)
# car2_copy.base_fare = 55

# print(car1_copy.calculateFare(14, variable))
# print(car2_copy.calculateFare(14, variable))