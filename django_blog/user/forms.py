from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from widgets import text_input, email_input, pass_input
from .models import User


class RegisterForm(forms.ModelForm):
    """Form used to `create` users"""

    def clean_password(self) -> str:
        """Hash the password on creation"""
        password = self.cleaned_data['password']
        password = make_password(password)

        return password

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
        ]

        widgets = {
            'first_name': text_input,
            'last_name': text_input,
            'username': text_input,
            'password': pass_input,
            'email': email_input,
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, widget=text_input)
    password = forms.CharField(max_length=255, widget=pass_input)

    def clean_username(self) -> str:
        """Check if the user exists"""
        username = self.cleaned_data['username']

        if not User.objects.filter(username=username).exists():
            # Message display is invalid username/password
            # to help mitigate against username enumeration
            # based on error messages
            raise forms.ValidationError('Invalid username/password')

        return username
