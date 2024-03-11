class Item:
    def __init__(self, name: str, price: float, quantity = 0):
        assert price >= 0, f"Price {self.price} can't be "
        assert quantity >= 0

        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Item: {self.name} \nPrice: {self.price} \nQuantity: {self.quantity}"

item1 = Item("Musfique", -10000, 13)
item_2 = Item("Headphone", 300, -12)
print(item1)
print(item_2)
print(type(item1.name))