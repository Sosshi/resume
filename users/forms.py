from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from django.forms import ModelForm

from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "", "id": "yourUsername"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "",
                "id": "yourPassword",
            }
        )
    )


class UserForm(ModelForm):
    required_css_class = "required"

    class Meta:
        model = CustomUser
        fields = [
            "profile_image",
            "first_name",
            "last_name",
            "date_of_birth",
            "about",
            "job",
            "address",
            "phone",
            "email",
            "twitter",
            "facebook",
            "instagram",
            "linkedin",
        ]
