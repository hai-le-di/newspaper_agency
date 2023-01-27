from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField()
    REQUIRED_FIELDS = ['email', 'years_of_experience', ]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Topic(models.Model):
    name = models.CharField(max_length=66)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=66)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    topic = models.ForeignKey(Topic,
                              related_name="newspapers",
                              on_delete=models.CASCADE)
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name="newspapers")

    def __str__(self):
        return f"{self.title} ({self.topic}, {self.published_date})"
