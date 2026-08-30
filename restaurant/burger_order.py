from chef import Chef

from order import Order
class BurgerOrder(Order):
    def __init__(self, cook:Chef):
        self.cook = cook
    
    def execute(self):
        print("burger order")
        self.cook.cook_burger()