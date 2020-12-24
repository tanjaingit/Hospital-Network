from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Post


class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body', 'post']
