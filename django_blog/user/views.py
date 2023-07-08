from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import User
from .forms import RegisterForm, LoginForm
from blog.models import Post


class Register(CreateView):
    model = User
    template_name = "user/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("user:login")


class Login(LoginView):
    template_name = "user/login.html"
    authentication_form = LoginForm

    def get_success_url(self):
        """
        Redirect to user profile on successful login
        """
        return reverse_lazy("user:profile", args=[self.request.user.slug])


class Profile(DetailView):
    model = User
    template_name = "user/profile.html"
    context_object_name = "profile_user"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["posts"] = Post.objects.filter(author=self.request.user)
        return context


class Logout(LogoutView):
    pass


# TODO Create view to delete user account
