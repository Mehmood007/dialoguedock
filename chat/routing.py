from django.urls import path

from .consumers import ChatComsumer

asgi_urlpatterns = [
    path('websocket', ChatComsumer.as_asgi(), name='chat'),
]
