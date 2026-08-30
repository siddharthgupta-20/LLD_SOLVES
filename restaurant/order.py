from chef import Chef
from abc import abstractmethod
class Order:
    @abstractmethod
    def execute(self):
        pass