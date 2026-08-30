from transportservice import TransportService
from bikemode import BikeMode
from carmode import CarMode

b = BikeMode()

service = TransportService(b)
service.eta()
service.directions()
service.set_mode(CarMode())
service.eta()
service.directions()