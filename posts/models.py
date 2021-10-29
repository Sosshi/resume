from django.db import models


class Tag(models.Model):
    """
    This is related to the creative writing model and will be used in seraching for articles"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CreativeWriting(models.Model):
    """
    This controls the model for the creative writing posts
    """

    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, related_name="creative_writings")
    body = models.TextField()

    def __str__(self):
        return self.title


class Acadamic(models.Model):
    title = models.CharField(max_length=255)
    year = models.DateField()
    body = models.TextField()

    def __str__(self):
        return self.title
