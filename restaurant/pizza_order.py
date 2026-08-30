from chef import Chef

from order import Order
class PizzaOrder(Order):
    def __init__(self, cook:Chef):
        self.cook = cook
    def execute(self):
        print("pizza order")
        self.cook.cook_pizza()