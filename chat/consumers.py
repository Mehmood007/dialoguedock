from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class Anything(WebsocketConsumer):
    def receive(self, text_data=None, bytes_data=None):
        print(self.channel_name)
        print(self.channel_layer.channels)
        async_to_sync(self.channel_layer.group_add)(
            'my_group', self.channel_name
        )

        event = {
            'type': 'send_to_specific_channel',
            'message': 'This is just demo message',
        }

        async_to_sync(self.channel_layer.group_send)('my_group', event)

    def send_to_specific_channel(self, event):

        self.send(event['message'])

    def send_demo(self, event):
        self.send(event['message'])
