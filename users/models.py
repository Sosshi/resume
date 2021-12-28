from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    job = models.CharField(max_length=100)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    profile_image = models.ImageField(upload_to="images", null=True, blank=True)
    about = models.TextField(
        validators=[MinLengthValidator(300, message="Please enter more text")]
    )
    number_of_projects_completed = models.IntegerField(default=0)
    cv_link = models.URLField(null=True, blank=True)

    def get_image(self):
        """To get the image url"""
        url = "http://127.0.01:8000/static"
        if self.profile_image:
            return url + self.profile_image.url
        else:
            return ""


class ActivityLog(models.Model):
    user = models.ForeignKey(CustomUser, related_name="logs", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=255)

    def __str__(self):
        return self.activity

    class Meta:
        ordering = ["-created"]
