from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


# Dashboard views
class DashBoardView(LoginRequiredMixin, TemplateView):
    template_name = "admin_area/dashboard.html"
    login_url = reverse_lazy("login")


# blogViews
class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = "admin_area/blog_create.html"
    model = Post
    fields = ["title", "subtitle", "body", "image"]
    success_url = "/dashboard/blog/"

    def form_valid(self, form):
        form.instance.author = get_user_model().objects.get(id=1)
        return super().form_valid(form)


class BlogEditView(LoginRequiredMixin, UpdateView):
    template_name = "admin_area/blog_edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "image"]
    success_url = "/dashboard/blog/"


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "admin_area/delete.html"
    success_url = "/dashboard/blog/"


class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "admin_area/blog_list.html"
    context_object_name = "posts"


# statistics Views


class StatisticsViews(LoginRequiredMixin, TemplateView):
    template_name = "admin_area/statistics.html"


class UserDetailView(LoginRequiredMixin, UpdateView):
    template_name = "admin_area/profile.html"
    model = get_user_model()
    fields = [
        "profile_image",
        "first_name",
        "last_name",
        "date_of_birth",
        "about",
        "job",
        "address",
        "phone",
        "email",
        "twitter",
        "facebook",
        "instagram",
        "linkedin",
    ]
    success_url = "/dashboard/"
