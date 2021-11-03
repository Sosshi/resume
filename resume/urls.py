from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("works/", include("posts.urls")),
    path("blog/", include("blog.urls")),
    path("user/", include("users.urls")),
    path("dashboard/", include("admin_area.urls")),
    path("users/", include("django.contrib.auth.urls")),
]
