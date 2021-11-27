from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    BlogListView,
    BlogDetailView,
    subscribe,
    BlogSearch,
    category_list_view,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="blog"),
    path("subscribe/", subscribe, name="subscribe"),
    path("search/", BlogSearch.as_view(), name="blog_search"),
    path("category/<str:slug>/", category_list_view, name="blog_category_filter"),
    path("<str:slug>/", BlogDetailView.as_view(), name="blog_detail"),
]
