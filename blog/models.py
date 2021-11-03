from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey(
        get_user_model(), related_name="posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    isPublished = models.BooleanField("Published?", default=False)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.slug)])

    def get_image(self):
        """To get the image url"""
        url = "http://127.0.01:8000/static"
        if self.image:
            return url + self.image.url
        else:
            return ""

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(" ", "-")
        super(Post, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(
        Post, related_name="categories", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
