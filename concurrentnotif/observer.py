from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def publish(self,msg):
        pass