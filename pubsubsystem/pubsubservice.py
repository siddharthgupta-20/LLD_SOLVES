

class PubSubService:
    def __init__(self):
        self.mapping = {}

    def send(self, topic, msg):
        if topic not in self.mapping:
            self.mapping[topic] = []
        for i in self.mapping[topic]:
            i.recieve(msg,topic)

    def subscribe(self,sub,topic):
        if self.mapping.get(topic,0) == 0:
            self.mapping[topic] = [sub]
        else:
            self.mapping[topic].append(sub)
    
