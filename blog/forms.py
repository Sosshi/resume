from django import forms
from django.forms import ModelForm
from .models import Post, Subscribers


class PostForm(ModelForm):
    required_css_class = "required"

    class Meta:
        model = Post
        fields = "__all__"


class SubscribersForm(ModelForm):
    required_css_class = "required"

    class Meta:
        model = Subscribers
        fields = "__all__"
