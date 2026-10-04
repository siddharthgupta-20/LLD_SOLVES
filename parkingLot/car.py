from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, license_plate: str,vtype = 'car'):
        self.vtype = 'car'
        super().__init__(license_plate)