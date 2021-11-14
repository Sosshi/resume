from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
    DetailView,
)
from django.db.models import Count

from blog.models import Post, Subscribers, Category
from blog.forms import PostForm
from users.models import ActivityLog


# Dashboard views
class DashBoardView(LoginRequiredMixin, TemplateView):
    template_name = "admin_area/dashboard.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        activity_log = ActivityLog.objects.all()[:5]
        number_of_blogs = Post.objects.count()
        number_of_blog_views = 0
        context["activity_logs"] = activity_log
        context["number_of_blogs"] = number_of_blogs
        context["number_of_blog_views"] = number_of_blog_views
        return context


# blogViews
class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = "admin_area/blog_create.html"
    model = Post
    fields = [
        "title",
        "subtitle",
        "category",
        "body",
        "image",
    ]
    success_url = "/dashboard/blog/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        ActivityLog.objects.create(
            user=self.request.user,
            activity=f"Arcticle {form.instance.title} was created",
        )
        return super().form_valid(form)


class BlogEditView(LoginRequiredMixin, UpdateView):
    template_name = "admin_area/blog_edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "image"]
    success_url = "/dashboard/blog/"

    def form_valid(self, form):
        ActivityLog.objects.create(
            user=self.request.user, activity=f"Artcile {form.instance.title} was edited"
        )
        return super().form_valid(form)


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        subscribers = Subscribers.objects.all()
        context["subscribers"] = subscribers
        return context


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


class CategoriesCreateView(CreateView):
    template_name = "admin_area/categories.html"
    model = Category
    fields = ["name"]
    success_url = "/dashboard/blog/categories/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class CategoriesDeleteView(DeleteView):
    template_name = "admin_area/category_delete.html"
    model = Category
    success_url = "/dashboard/blog/categories/"


class SearchView(ListView):
    template_name = "admin_area/search.html"
    context_object_name = "posts"
    model = Post

    def get_queryset(self):
        title = self.kwargs.get("title", "")
        object_list = self.model.objects.all()
        if title:
            object_list = object_list.filter(title__icontains=title)
        return object_list
