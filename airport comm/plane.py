
class Plane:
    def __init__(self,number, tower):
        self.__number = number
        self.__tower = tower
        self.__tower.add_plane(self)
    def get_number(self):
        return self.__number


    def send_msg (self,msg):
        self.__tower.send_msg(msg,self)

    def recieve_msg(self,msg,whosent:"Plane"):
        print(f"{self.__number} got {msg} from {whosent.__number}")