import csv

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity=0):
        assert price >= 0, f"price {price} should be greater or equal to zero"
        assert quantity >= 0, f"quantity {quantity} should be greater or equal to zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def calculate_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("data.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for i in items:
            # print(i)
            Item(
                name = i.get('name'),
                price = float(i.get('price')),  # Convert to float
                quantity = int(i.get('quantity')),  # Convert to int
            )

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"

Item.instantiate_from_csv()
print(Item.all)
