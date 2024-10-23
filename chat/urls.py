from django.urls import path

from .views import (
    ChatPersonView,
    HomeView,
    LoginView,
    LogoutView,
    MainView,
    RegisterView,
)

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('home', HomeView.as_view(), name='home'),
    path('chat_person/<int:id>', ChatPersonView.as_view(), name='chat_person'),
]
