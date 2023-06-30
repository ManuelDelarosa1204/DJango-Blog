from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .models import User
from .forms import RegisterForm, LoginForm


class Index(TemplateView):
    template_name = 'index.html'


class Register(CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('user:login')


class Login(LoginView):
    template_name = 'user/login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        """
        Redirect to user profile on successful login
        """
        return reverse_lazy('user:profile', args=[self.request.user.slug])


class Profile(DetailView):
    model = User
    template_name = 'user/profile.html'
    context_object_name = 'profile_user'


class Logout(LogoutView):
    pass
