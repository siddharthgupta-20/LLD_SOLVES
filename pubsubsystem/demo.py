from publisher import Publisher
from subscriber import Subscriber
from topic import Topic
from pubsubservice import PubSubService
class PubSubDemo:
    def run():
        p1 = Publisher()
        p2 = Publisher()

        s1 = Subscriber()
        s2 = Subscriber()

        t1  = Topic("lala")
        t2  = Topic("football")

        service  = PubSubService()

        service.subscribe(s1,t1)
        service.subscribe(s2,t2)
        
        msg ="messi"
        p1.publish(service, msg, t1)



if __name__ == "__main__":
    PubSubDemo.run()


