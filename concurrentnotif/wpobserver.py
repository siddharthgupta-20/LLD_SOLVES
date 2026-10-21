from observer import Observer

class WPObserver(Observer):
    def publish(self,msg):
        print("publish via whatsapp")