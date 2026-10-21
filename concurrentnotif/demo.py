import asyncio

from mailobserver import MailObserver
from wpobserver import WPObserver
from messageobserver import MessageObserver

from service import NotificationService

mail = MailObserver()
msg = MessageObserver()
wp = WPObserver()

service = NotificationService()

service.add_observer(mail)
service.add_observer(msg)
service.add_observer(wp)

asyncio.run(service.send("ahahahaha"))