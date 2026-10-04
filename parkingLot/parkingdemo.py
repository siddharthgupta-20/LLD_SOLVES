from parkinglotservice import ParkingLotService
from parkinglot import ParkingLot
from bike import Bike
from car import Car
from parkingspace import ParkingSpace

a1 = ParkingSpace(0,"car",1)
b1 = ParkingSpace(0,"car",2)
c1 = ParkingSpace(0,"car",3)

a2 = ParkingSpace(0,"bike",1)
b2 = ParkingSpace(0,"bike",2)
c2 = ParkingSpace(0,"bike",3)

lot = ParkingLot()
lot.add_space(a1)
lot.add_space(b1)
lot.add_space(c1)

lot.add_space(a2)
lot.add_space(b2)
lot.add_space(c2)

service = ParkingLotService()

car = Car("123")
bike = Bike("456")
print(lot.get_availability())

service.register_vehicle(bike,lot)
service.register_vehicle(car,lot)

print(lot.get_availability())
lot.status()