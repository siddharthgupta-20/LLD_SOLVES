
class Publisher:
    def __init__(self):
        pass

    def publish(self,svc, msg,topic):
        svc.send(topic,msg)