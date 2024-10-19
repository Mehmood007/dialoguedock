from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        channel_layer = get_channel_layer()
        event = {
            'type': 'send_demo',
            'message': 'hi this message is sent from views',
        }

        async_to_sync(channel_layer.group_send)('my_group', event)
        return super().get(request, *args, **kwargs)


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class LogoutView(TemplateView):
    template_name = 'main.html'


class HomeView(TemplateView):
    template_name = 'home.html'


class ChatPersonView(TemplateView):
    template_name = 'chat_person.html'
