from order import Order

class Waiter:
    def __init__(self):
        pass
    def takeorder(self, order: Order):
        order.execute()