"""Widgets to be used in forms"""

from django import forms

attrs = {'class': 'form-control'}

text_input = forms.TextInput(attrs=attrs)
text_area = forms.Textarea(attrs=attrs)
email_input = forms.EmailInput(attrs=attrs)
pass_input = forms.PasswordInput(attrs=attrs)
select_input = forms.Select(attrs={'class': 'form-select'})
