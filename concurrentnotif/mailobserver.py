from observer import Observer

class MailObserver(Observer):
    def publish(self,msg):
        print("publish via mail")