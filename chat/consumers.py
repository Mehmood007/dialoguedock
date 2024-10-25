import json
from datetime import date, datetime

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User

from .models import Message


class ChatComsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            f'chat_{self.scope['user'].id}', self.channel_name
        )

        return super().connect()

    def receive(self, text_data=None, bytes_data=None):
        other_person_id = self.scope['url_route']['kwargs']['id']
        other_user = User.objects.get(id=other_person_id)
        data = json.loads(text_data)
        message = data.get('message')
        new_message = Message()
        new_message.message = message
        new_message.sender = self.scope['user']
        new_message.receiver = other_user
        new_message.date = date.today()
        new_message.time = datetime.now().strftime('%H:%M:%S')
        new_message.save()
        try:
            event = {
                'type': 'send_to_specific_channel',
                'message': message,
            }

            async_to_sync(self.channel_layer.group_send)(
                f'chat_{other_person_id}', event
            )
        except:
            pass

    def send_to_specific_channel(self, event):
        self.send(event['message'])
