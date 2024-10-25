from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from .models import Message


class MainView(TemplateView):
    template_name = 'main.html'


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request: HttpRequest) -> HttpResponse:
        data = request.POST.dict()
        user = authenticate(
            request,
            username=data.get('username'),
            password=data.get('password'),
        )
        if user != None:
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {'error': 'Invalid Credentials'})


class RegisterView(TemplateView):
    template_name = 'register.html'

    def post(self, request: HttpRequest) -> HttpResponse:
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken', None)
        user = User(**data)
        user.set_password(request.POST['password'])
        try:
            user.save()
        except:
            context = {'error': 'something wrong with data'}
            return render(request, 'register.html', context)

        user = authenticate(
            request=request, username=user.username, password=data['password']
        )
        login(request, user)

        return redirect('home')


class LogoutView(TemplateView):
    template_name = 'main.html'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        logout(request)
        return super().get(request, *args, **kwargs)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        users = User.objects.all()
        return {
            'users': users,
        }


class ChatPersonView(LoginRequiredMixin, TemplateView):
    template_name = 'chat_person.html'

    def get_context_data(self, **kwargs):
        person = get_object_or_404(User, id=kwargs.get('id'))
        messages = Message.objects.filter(
            (Q(sender=self.request.user) & Q(receiver=person))
            | (Q(sender=person) & Q(receiver=self.request.user))
        ).order_by('date', 'time')
        return {
            'messages': messages,
            'person': person,
        }
