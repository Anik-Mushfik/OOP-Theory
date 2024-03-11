class Customer:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.orders = []


#(b)
class Pastry:
    def __init__(self, weight, per_kg_price):
        self.weight = weight
        self.per_kg_price = per_kg_price
        self.cost = 0

#(c)
    def add_frosting(self, type):
        if (type == "Butter Cream"):
            self.cost += 400 * self.weight
        elif (type == "Whipped Cream"):
            self.cost += 200 * self.weight
        else:
            print(f"Frosting not available!!!")


    def total_cost(self):
        return self.cost + (self.weight * self.per_kg_price)
    

class Chocolate(Pastry):
    def __init__(self, weight):
        super().__init__(weight, 500)

    def __str__(self):
        return f"Cake: Chocoate cake \nWeight:{self.weight}; Price:{self.total_cost()}"

class Vanilla(Pastry):
    def __init__(self, weight):
        super().__init__(weight, 400)

    def __str__(self):
        return f"Cake: Vanilla cake \nWeight:{self.weight}; Price:{self.total_cost()}"


class Order:
    def __init__(self, type, quantity, weight):
        self.pastry_type = type
        self.quantity = quantity
        self.weight = weight
        self.price = 0
            

    def make_cake(self, frosting):
        if self.pastry_type == "Chocolate":
            self.pastry = Chocolate(self.weight)
        else:
            self.pastry = Vanilla(self.weight)
        
        # frosting = input("What frosting do you want? (Butter Cream / Whipped Cream / None) \n=>")
        if frosting != "None":
            self.pastry.add_frosting(frosting)

    def total_price(self):
        self.price += self.quantity * self.pastry.total_cost()

    def add_to_cart(self, customer):
        for i in range(self.quantity):
            customer.orders.append(self.pastry)
    

def creatOrder(cus):
    print(f"Customer Information: \nName:{cus.name} \nLocation:{cus.city} \n##########\nOrder Information:")
    for i in cus.orders:
        print(i)


c1 = Customer("Tasu", "Uttora Gram")
o_1 = Order("Chocolate", 1, 2)
o_1.make_cake("Butter Cream")
o_1.add_to_cart(c1)

creatOrder(c1)