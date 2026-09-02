from mediator import Mediator
from plane import Plane
from typing import List

class Tower(Mediator):
    def __init__(self):
        self.__planes = []

    def add_plane(self,plane:Plane):
        self.__planes.append(plane)

    def send_msg(self,msg,plane):
        for i in self.__planes:
            if i != plane:
                i.recieve_msg(msg,plane)
    
    