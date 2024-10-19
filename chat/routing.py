from django.urls import path

from .consumers import Anything

asgi_urlpatterns = [
    path('websocket', Anything.as_asgi(), name='anything'),
]
