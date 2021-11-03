from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Post
        fields = '__all__'