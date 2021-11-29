from django.db import models


class Education(models.Model):
    heading = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        ordering = ["-from_date"]

    def __str__(self):
        return self.heading


class Experience(models.Model):
    position = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    description = models.TextField()
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["-from_date"]

    def __str__(self):
        return self.position


class Skill(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.PositiveIntegerField()

    class Meta:
        ordering = ["-from_date"]

    def __str__(self):
        return self.name
