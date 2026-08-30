from abc import abstractmethod
class DiscountStategy:
    def __init__(self):
        pass
    @abstractmethod
    def get_discount(self):
        pass