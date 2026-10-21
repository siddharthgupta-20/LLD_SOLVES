from observer import Observer

class MessageObserver(Observer):
    def publish(self,msg):
        print("publish via message")