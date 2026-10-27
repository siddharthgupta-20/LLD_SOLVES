from topic import Topic
class Subscriber:
    def __init__(self):
        pass

    def recieve(self,msg,topic: Topic):
        print(f"recieved {msg} from {topic.name}")