from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mass_mail, BadHeaderError
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

from posts.models import Education, Experience, Skill, Work

from .forms import MailForm


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
        "cv_link",
        "number_of_projects_completed",
    ]
    success_url = "/dashboard/profile/1/"


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


class MailCreateView(TemplateView):
    template_name = "admin_area/mail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MailForm()
        return context


def send_email(request):
    mail_from = request.POST.get("mail_from")
    content = request.POST.get("content")
    email_list = Subscribers.objects.values_list("email", flat=True)
    list_of_mail = []
    for index, email in enumerate(email_list):
        list_of_mail.append(email)
    try:
        message = ("All lives matter", content, mail_from, list_of_mail)
        send_mass_mail((message,), fail_silently=True)
        return HttpResponse(
            """
        <div class="alert alert-primary alert-dismissible fade show" role="alert">
                Mail Sent Successfully!
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>"""
        )
    except:
        return HttpResponse(
            """<div class="alert alert-danger alert-dismissible fade show" role="alert">
                <i class="bi bi-exclamation-octagon me-1"></i>
                Something went wrong
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
              </div>"""
        )


class EducationCreateView(CreateView):
    model = Education
    template_name = "admin_area/education_create.html"
    fields = "__all__"
    success_url = "/dashboard/education/create/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["education"] = Education.objects.all
        return context


class EducationEditView(UpdateView):
    model = Education
    success_url = "/dashboard/education/create/"
    template_name = "admin_area/blog_edit.html"
    fields = "__all__"


class EducationDeleteView(DeleteView):
    model = Education
    success_url = "/dashboard/education/create/"
    template_name = "admin_area/category_delete.html"


class ExperienceCreateView(CreateView):
    model = Experience
    template_name = "admin_area/experience_create.html"
    fields = "__all__"
    success_url = "/dashboard/experience/create/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["experiences"] = Experience.objects.all
        return context


class ExperienceEditView(UpdateView):
    model = Experience
    success_url = "/dashboard/education/create/"
    template_name = "admin_area/blog_edit.html"
    fields = "__all__"


class ExperienceDeleteView(DeleteView):
    model = Experience
    success_url = "/dashboard/experience/create/"
    template_name = "admin_area/category_delete.html"


class SkillCreateView(CreateView):
    model = Skill
    template_name = "admin_area/skill_create.html"
    fields = "__all__"
    success_url = "/dashboard/skill/create/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["skills"] = Skill.objects.all
        return context


class SkillDeleteView(DeleteView):
    model = Skill
    template_name = "admin_area/category_delete.html"
    success_url = "/dashboard/skill/create/"


class SkillEditView(UpdateView):
    model = Skill
    success_url = "/dashboard/education/create/"
    template_name = "admin_area/blog_edit.html"
    fields = "__all__"


class WorksCreateView(CreateView):
    model = Work
    template_name = "admin_area/work_create.html"
    fields = "__all__"
    success_url = "/dashboard/work/create/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["works"] = Work.objects.all
        return context


class WorkDeleteView(DeleteView):
    model = Work
    template_name = "admin_area/category_delete.html"
    success_url = "/dashboard/work/create/"


class WorkEditView(UpdateView):
    model = Work
    success_url = "/dashboard/work/create/"
    template_name = "admin_area/blog_edit.html"
    fields = "__all__"
