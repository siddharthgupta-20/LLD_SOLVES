from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, license_plate: str):
        self.vtype = 'bike'
        super().__init__(license_plate)