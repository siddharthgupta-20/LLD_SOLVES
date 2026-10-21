import asyncio


class NotificationService:
    def __init__(self):
        self.observer = []

    def add_observer(self,observer):
        self.observer.append(observer)

    async def send(self, msg):
        await asyncio.gather(
            *(asyncio.to_thread(observer.publish, msg) for observer in self.observer)
        )

 