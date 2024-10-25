from django.urls import path

from .consumers import ChatComsumer

asgi_urlpatterns = [
    path('websocket/<int:id>', ChatComsumer.as_asgi(), name='chat'),
]
