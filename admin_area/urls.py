from django.urls import path
from .views import (
    DashBoardView,
    BlogListView,
    BlogCreateView,
    BlogEditView,
    BlogDeleteView,
    StatisticsViews,
    UserDetailView,
    CategoriesCreateView,
    CategoriesDeleteView,
    SearchView,
)

urlpatterns = [
    # DashBoard
    path("", DashBoardView.as_view(), name="dashboard"),
    # Search
    path("search/", SearchView.as_view(), name="search"),
    # BlogList
    path("blog/categories/", CategoriesCreateView.as_view(), name="categories"),
    path(
        "blog/categories/delete/<int:pk>/",
        CategoriesDeleteView.as_view(),
        name="categories_delete",
    ),
    path("blog/", BlogListView.as_view(), name="dashboard_blog_list"),
    path("blog/create/", BlogCreateView.as_view(), name="dashboard_blog_create"),
    path("blog/edit/<str:slug>/", BlogEditView.as_view(), name="dashboard_blog_edit"),
    path(
        "blog/delete/<str:slug>/",
        BlogDeleteView.as_view(),
        name="dashboard_blog_delete",
    ),
    # Statisticts
    path("statistics/", StatisticsViews.as_view(), name="dashboard_statistics"),
    path("profile/<int:pk>/", UserDetailView.as_view(), name="dashboard_profile"),
]
