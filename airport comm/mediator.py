# mediator
from plane import Plane
from  abc import ABC, abstractmethod
class Mediator(ABC):
    @abstractmethod
    def add_plane(plane: Plane):
        pass
    def send_msg(self):
        pass