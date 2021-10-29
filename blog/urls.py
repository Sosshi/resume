from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import BlogListView, BlogDetailView

urlpatterns = [
    path("", BlogListView.as_view(), name="blog"),
    path("<str:slug>/", BlogDetailView.as_view(), name="blog_detail"),
] + static(settings.MEDIA_URLS, document_root=settings.MEDIA_ROOT)
