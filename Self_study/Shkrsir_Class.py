## Shallow Copy:
class A:
    pass

a= A()
a.name = "UIU"
print(a.name)
b=a
print(b.name)
b.name = "United"
print(a.name)
print(b.name)

## Deep Copy:
import copy
class A:
    pass
a= A()
a.name = "UIU"
b= copy.deepcopy(a)
print(b.name)
b.name = "United"
print(a.name)
print(b.name)

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
    def __init__(self, name, points, health, location, amo, vest_level):
        self.name = name
        self.points = points
        self.health = health
        self.location = location
        self.amo = amo
        self.vest_level = vest_level

    def describe_player(self):
        print(f'''
Player name: {self.name.title()}
Health: {self.health}
Amo: {self.amo}
Vest: Level {self.vest_level} vest
''')

    def combat(self, hit, killed):
        self.health -= (hit * 2.5)
        self.points -= (hit * 5)
        self.points += (killed * 10)

    def amo_left(self, shoot):
        self.amo -= shoot
        if (self.amo < 30):
            print(f"{self.name} has only one mag left. Needs Backup!!!")
    
    def will_die(self):
        if (self.health > 50) and (self.vest_level <= 3):
            print(f"{self.name} is doing a great job.. Keep fighting!!!")
        elif (self.health < 50) and (self.vest_level < 3):
            print(f"{self.name} is in critical condition. Needs painkiller!!!")
        elif (self.health < 25) and (self.vest_level < 2):
            print(f"{self.name} is in critical condition. Needs treatment and new vest!!!")
        elif (self.health == 0) and (self.vest_level == 0):
            print(f"{self.name} DIED!!!!!")
            
    def tracker(self, tracked_location):
        if (self.location == tracked_location):
            print(f"Your location has been exposed!!! Fall back to the safe zone.")

    def results(self):
        if (self.health > 0):
            print(f'''\nGame is Over!!!
Player: {self.name}
Health left: {self.health}
Score: {self.points}

Congratulations!!! You Won!!! GG!!!!!
''')
        else:
            print(f'''\nGame is Over!!!
Player: {self.name}
Health left: {self.health}
Score: {self.points}

You Lost!!! Better luck next time!!!
''')


player_1 = Player("Musfique", 500, 100, "Mirpur", 78, 2)
player_1.describe_player()
player_1.combat(15, 8)
player_1.amo_left(70)
player_1.will_die()
player_1.tracker("Mirpur")
player_1.results()



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

record = {}

class Person:
    def __init__(self, name, address, phoneNumber, birthday):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
        self.birthday = birthday
        
    def record_entry(self):
        record[self.name] = {'Address': self.address, 
                            'Phone Number': self.phoneNumber, 
                            'Birthday': self.birthday}
        

def search(serarch_person):
    for i in record.keys():
        if i == serarch_person:
            print(f"Name: {i}\n{record[i]}")


person_1 = Person("Musfique", "Mirpur 12", "01_________", "7 May, 2002")
person_2 = Person("Tasfiya", "Rampura", "01_________", "9 July, 2002")
person_3 = Person("Anas", "Dhanmondi", "01_________", "20 March, 2003")
person_4 = Person("Abid", "Mirpur 12", "01_________", "17 Dec, 2002")
person_1.record_entry()
person_2.record_entry()
person_3.record_entry()
person_4.record_entry()

search("Musfique")