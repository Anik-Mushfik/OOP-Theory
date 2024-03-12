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
        self.cost = self.weight * self.per_kg_price

#(c)
    def add_frosting(self, type, quantity):
        if (type == "Butter Cream"):
            self.cost += 400 * quantity
        elif (type == "Whipped Cream"):
            self.cost += 200 * quantity
        else:
            print(f"Frosting not available!!!")
    


class Chocolate(Pastry):
    def __init__(self, weight):
        super().__init__(weight, 500)

    def __str__(self):
        return f"Cake: Chocoate cake \nWeight:{self.weight}; Price:{self.cost}"

class Vanilla(Pastry):
    def __init__(self, weight):
        super().__init__(weight, 400)

    def __str__(self):
        return f"Cake: Vanilla cake \nWeight:{self.weight}; Price:{self.cost}"


class Order:
    def __init__(self, type, quantity, weight):
        self.pastry_type = type
        self.quantity = quantity
        self.weight = weight
        self.price = 0
            

    def creatOrder(self, frosting=None, frosting_qantity=0):
        if self.pastry_type == "Chocolate":
            self.pastry = Chocolate(self.weight)
        else:
            self.pastry = Vanilla(self.weight)
        
        # frosting = input("What frosting do you want? (Butter Cream / Whipped Cream / None) \n=>")
        # if frostring != "None":
        if frosting:
            self.pastry.add_frosting(frosting, frosting_qantity)

    def total_price(self):
        self.price += self.quantity * self.pastry.total_cost()

    def add_to_cart(self, customer):
        for i in range(self.quantity):
            customer.orders.append(self.pastry)
    

def printRecipt(cus):
    bill = 0
    print(f"Customer Information: \nName:{cus.name} \nLocation:{cus.city} \n====================\nOrder Information:")
    for i in cus.orders:
        print(i)
        bill += i.cost
    print(f"======================= \nTotal Bill: {bill}")


# Creat a customer profile.
c1 = Customer("Tasu", "Uttora Gram")
# Order your cake.
o_1 = Order("Chocolate", 1, 2)
# Confirm the order with add-ons
o_1.creatOrder("Butter Cream", .5)
# Add the order to cart
o_1.add_to_cart(c1)
o_2 = Order("Vanilla", 2, 1.5)
o_2.creatOrder()
o_2.add_to_cart(c1)

# Print the bill recipt for the customer
printRecipt(c1)