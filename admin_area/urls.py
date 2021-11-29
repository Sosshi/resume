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
    MailCreateView,
    send_email,
    EducationCreateView,
    ExperienceCreateView,
    SkillCeateView,
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
    # subscribers
    path("subscribers/", StatisticsViews.as_view(), name="dashboard_statistics"),
    path("subscribers/mail/", MailCreateView.as_view(), name="dashboard_send_mail"),
    path("subscribers/main/send/", send_email, name="dashboard_send"),
    path("profile/<int:pk>/", UserDetailView.as_view(), name="dashboard_profile"),
    # Works
    path(
        "education/create/",
        EducationCreateView.as_view(),
        name="dashboard_education_create",
    ),
    path(
        "experience/create/",
        ExperienceCreateView.as_view(),
        name="dashboard_experience_create",
    ),
    path("skill/create/", SkillCeateView.as_view(), name="dashboard_skill_create"),
]
