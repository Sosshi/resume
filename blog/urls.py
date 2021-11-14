from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import BlogListView, BlogDetailView, subscribe

urlpatterns = [
    path("", BlogListView.as_view(), name="blog"),
    path("subscribe/", subscribe, name="subscribe"),
    path("<str:slug>/", BlogDetailView.as_view(), name="blog_detail"),
]
