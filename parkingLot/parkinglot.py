from parkingspace import ParkingSpace
from vehicle import Vehicle
class ParkingLot:
    def __init__(self):
        self.availablespace = []
        self.occupiedspace = {}
    def add_space(self,space:ParkingSpace):
        self.availablespace.append(space)

    def get_availability(self):
        for i in self.availablespace:
            print(i.number,i.vtype,i.level)

    def assign_space(self,vehicle:Vehicle):
        for i in self.availablespace:
            if i.vtype == vehicle.vtype:
                self.occupiedspace[vehicle] = i
                return (i.number,i.level)

    def empty_space(self,vehicle):
        temp  =self.occupiedspace[vehicle]
        del self.occupiedspace[vehicle]
        self.availablespace.append(temp)
    def status(self):
        print(self.occupiedspace)

