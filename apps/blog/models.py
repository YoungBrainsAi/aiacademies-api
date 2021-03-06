from django.contrib.auth.models import User
from django.db import models

from aiacademies_api import settings


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    banner_image = models.URLField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, related_name='posts', null=True)
    featured = models.BooleanField(default=False)
    posted = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
