from transportmode import TransportMode

class CarMode(TransportMode):
    def __init__(self):
        self.__eta = 10
        self.__directions = ["up","down","up", "down"]

    def eta(self):
        return self.__eta
    def directions(self):
        return self.__directions