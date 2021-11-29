from django.urls import path
from .views import WorksPage

urlpatterns = [
    path("", WorksPage.as_view(), name="works"),
]
