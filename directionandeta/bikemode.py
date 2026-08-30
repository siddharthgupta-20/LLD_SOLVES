from transportmode import TransportMode

class BikeMode(TransportMode):
    def __init__(self):
        self.__eta = 15
        self.__directions = ["left","right","right", "left"]

    def eta(self):
        return self.__eta
    def directions(self):
        return self.__directions