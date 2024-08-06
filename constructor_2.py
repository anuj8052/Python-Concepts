class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity = 0):

        assert price >= 0, f"price {price} should be grater or equal to zero"
        assert quantity >=0, f"quantity {quantity} should be greater or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price*self.quantity
    
    def calculate_discount(self):
        self.price = self.price*self.quantity*self.pay_rate

    # def __repr__(self) -> str:
    #     return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
    
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
        


item1 = Item("phone", 500, 5)
item1 = Item("Laptop", 1000, 3)
item1 = Item("Cable", 10, 5)
item1 = Item("Mouse", 50, 5)
item1 = Item("phone", 75, 5)

print(Item.all)

# accessing the elements values from the list
# for instance in Item.all:
#     # print(instance.name, instance.price, instance.quantity)
#     print(instance.name)
#     print(instance.price)
#     print(instance.quantity)



