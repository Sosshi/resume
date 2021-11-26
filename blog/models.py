from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount
from django.db.models.signals import post_save
from django.core.mail import send_mass_mail


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        """Slugify and fill in the slug model"""
        self.name = self.name.lower()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        get_user_model(), related_name="posts", on_delete=models.PROTECT
    )
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    isPublished = models.BooleanField("Published?", default=False)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    slug = models.SlugField(default="", editable=False, max_length=160)
    post_views = GenericRelation(
        HitCount,
        object_id_field="object_pk",
        related_query_name="hit_count_generic_relation",
    )
    category = models.ForeignKey(
        Category, related_name="posts", on_delete=models.DO_NOTHING
    )

    def get_absolute_url(self):
        """Blog post reverse Url"""
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
        """Slugify and fill in the slug model"""
        self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)


class Subscribers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def send_emails(sender, instance, **kwargs):
    email_list = Subscribers.objects.values_list("email", flat=True)
    list_of_mail = []
    for index, email in enumerate(email_list):
        list_of_mail.append(email)
    try:
        message = (instance.title, instance.body, "symon@gmail.com", list_of_mail)
        send_mass_mail((message,), fail_silently=True)

    except:
        pass


post_save.connect(send_emails, sender=Post)
