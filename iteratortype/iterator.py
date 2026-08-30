from abc import abstractmethod
class Iterator:
    @abstractmethod
    def has_next(self):
        pass
    @abstractmethod
    def next(self):
        pass