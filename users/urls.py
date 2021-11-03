from django.contrib.auth import views
from django.urls import path

from .forms import UserLoginForm

urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(
            template_name="login.html", authentication_form=UserLoginForm
        ),
        name="login",
    )
]
