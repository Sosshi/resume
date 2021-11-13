from django.db import models


class News(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    source = models.CharField(max_length=100)
    link = models.URLField()
    date = models.DateTimeField()

    def __str__(self):
        return self.heading
