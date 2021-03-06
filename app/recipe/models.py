from django.db import models
from django.conf import settings

class Tag(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=264)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,#if you delete user, delete this tag too
    )

    def __str__(self):
        return self.name