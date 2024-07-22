class Item:
    def __init__(self, name, price, quantity):
        # print(f"An instance is created: {name}")
        # I can assign dynamic atributes in this __init__ method to reduce the hardcoded code or we can say complexity
        # we also call __init__ method as a constructor
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, x, y):
        return x*y
    

item1 = Item("phone", 500, 5)
# item1.name = "phone"
# item1.price = 500
# item1.quantity = 10


item2 = Item("Laptop", 1000, 3)
# item2.name = "Laptop" after assigning name in magic method I don't have to write these lines, now I can do for rest of the lines below
# item2.price = 1000
# item2.quantity = 3

print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.price*item1.quantity)
print(item2.name)
print(item2.price)
print(item2.quantity)
print(item2.price*item2.quantity)

