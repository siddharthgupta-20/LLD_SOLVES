from abc import ABC,abstractmethod
class TransportMode(ABC):
    @abstractmethod
    def eta(self):
        pass
    def directions(self):
        pass