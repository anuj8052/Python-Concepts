# freecodecanmp
# https://www.youtube.com/watch?v=Ej_02ICOIgs&ab_channel=freeCodeCamp.org
class Item:
    pay_rate = 0.8 #this is a class attribute and the payrate after 20% discount

    def __init__(self, name: str, price: float, quantity = 0): #quantity default as 0

        # suppose you naver want to recieve negative number of price as well as quantity
        # there is a method for this also
        # run validations to the recieved arguments

        assert price >= 0, f"price {price} is not greater or equal to zero"
        assert quantity>=0, f"Quantity {quantity} is not greater or equal to zero"

        
        # assign to self self object
        # print(f"An instance is created: {name}")
        # I can assign dynamic atributes in this __init__ method to reduce the hardcoded code or we can say complexity
        # we also call __init__ method as a constructor
        self.name = name
        self.price = price
        self.quantity = quantity

        


    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        # self.price = self.price*Item.pay_rate #if we are overriding the pay_rate in any instance it will not change cuz it is recieving att. from class
        self.price = self.price*self.pay_rate # now we can override the pay_rate value in instance 
    

item1 = Item("phone", 500, 5)
# item1.name = "phone"
# item1.price = 500
# item1.quantity = 10


item2 = Item("Laptop", 1000, 3)
# item2.name = "Laptop" after assigning name in magic method I don't have to write these lines, now I can do for rest of the lines below
# item2.price = 1000
# item2.quantity = 3

"""
output for init method
print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.price*item1.quantity)
print(item2.name)
print(item2.price)
print(item2.quantity)
print(item2.price*item2.quantity)
"""

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# output for class atributes
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)
# print(Item.pay_rate*item1.price*item1.quantity)
# print(Item.pay_rate*item2.price*item2.quantity)
# print(Item.__dict__) #this will give all the attributes for class level
# print(item1.__dict__) #this will give all the attributes for instance level

# discount function calling
item1.apply_discount()
print(item1.price) # 400 for this its same cuz we haven't override the pay_rate

item2.pay_rate = 0.7 #overridin the pay rate
item2.apply_discount()
print(item2.price) #700










