from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from .models import Post, Category
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
    if request.method == "POST":
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
