from django import forms
from .models import Post, Comment
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


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = [
            'comment',
        ]

        widgets = {
            'comment': text_area
        }
