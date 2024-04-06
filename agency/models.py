from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255)


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")
