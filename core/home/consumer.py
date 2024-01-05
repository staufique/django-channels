from channels.generic.websocket import WebsocketConsumer


#we are creating WebSocketConsumer class 
class TestConsumer(WebsocketConsumer):

    def connect(self):
        pass

    def receive(self):
        pass

    def disconnect(self):
        pass