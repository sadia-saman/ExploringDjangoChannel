from channels.generic.websocket import WebsocketConsumer
import json
from time import sleep
from random import randint


class RealTimeConsumer(WebsocketConsumer):
    def connect(self):
        self.accept() 
        
        for i in range(1000):
            self.send(json.dumps({'value': randint(-100,100)}))
            sleep(1)

    