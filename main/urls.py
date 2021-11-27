from django.urls import path
from .views import HomePage, ContactPage, contact, Aboutpage, WorksPage

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("contact/", ContactPage.as_view(), name="contact"),
    path("send/", contact, name="contact_davie"),
    path("works/", WorksPage.as_view(), name="works"),
    path("about/", Aboutpage.as_view(), name="about"),
]
