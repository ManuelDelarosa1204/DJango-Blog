"""Widgets to be used in forms"""

from django import forms

attrs = {'class': 'form-control'}

text_input = forms.TextInput(attrs=attrs)
email_input = forms.EmailInput(attrs=attrs)
pass_input = forms.PasswordInput(attrs=attrs)
