from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatComsumer(WebsocketConsumer):
    def receive(self, text_data=None, bytes_data=None):
        event = {
            'type': 'send_to_specific_channel',
            'message': 'This is just demo message',
        }

        async_to_sync(self.channel_layer.send)(self.channel_name, event)

    def send_to_specific_channel(self, event):
        self.send(event['message'])
