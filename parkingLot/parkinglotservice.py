from parkinglot import ParkingLot
from parkingspace import ParkingSpace
from vehicle import Vehicle
from threading import Lock
class ParkingLotService:
    _lock = Lock()
    def register_vehicle(self,vehicle,parkinglot:ParkingLot) -> Vehicle:
        with self._lock:
            g = parkinglot.assign_space(vehicle)
            print(g)
