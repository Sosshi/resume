from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("works/", include("posts.urls")),
    path("blog/", include("blog.urls")),
    path("user/", include("users.urls")),
    path("dashboard/", include("admin_area.urls")),
    path("users/", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
