from django import forms
from .models import Post
from widgets import text_input, text_area, select_input


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = [
            'title',
            'body',
            'status',
        ]

        widgets = {
            'title': text_input,
            'body': text_area,
            'status': select_input,
        }
