import time

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from django.db.models import Q

from .models import Post, Category, Subscribers
from .forms import SubscribersForm


class BlogListView(ListView):
    template_name = "blog.html"
    model = Post
    context_object_name = "posts"


class BlogDetailView(DetailView):
    template_name = "blog_detail.html"
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        post = context["object"]
        posts = Post.objects.all()[:4]
        categories = Category.objects.all()
        context["post"] = post
        context["posts"] = posts
        context["categories"] = categories
        return context


def subscribe(request):
    email = request.POST.get("email")
    first_name = request.POST.get("firstname")
    last_name = request.POST.get("lastname")

    if email and first_name and last_name:
        try:
            Subscribers.objects.create(
                email=email, first_name=first_name, last_name=last_name
            )
            return HttpResponse("Subscribed successfully")
        except:
            return HttpResponse("Subscription failed")


class BlogSearch(ListView):
    model = Post
    template_name = "blog.html"
    context_object_name = "posts"

    def get_queryset(self):
        search_item = self.request.GET.get("q")
        objects_list = Post.objects.filter(
            Q(title__icontains=search_item)
            | Q(subtitle__icontains=search_item)
            | Q(body__icontains=search_item)
        )

        return super().get_queryset()


def category_list_view(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category)

    return render(request, "blog.html", {"posts": posts})
