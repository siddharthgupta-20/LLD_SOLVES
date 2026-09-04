from laptop import Laptop

class LaptopBuilder:
    def __init__(self):
        self.__laptop = Laptop()

    def build_color(self,type):
        self.__laptop.color = type
        return self
    def build_graphic(self,type):
            self.__laptop.graphic = type
            return self
    def build_ram(self,type):
            self.__laptop.ram = type
            return self
    
    def build_processor(self,type):
            self.__laptop.processor = type
            return self

    def build(self):
          return self.__laptop