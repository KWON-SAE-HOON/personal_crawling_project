from django.db import models
from django.contrib.auth.models import AbstractUser


class SteamUser(AbstractUser):
    steam_id = models.CharField(max_length=17)
    name = models.CharField(max_length=200)
    profile_url = models.URLField()
    avatar_url = models.URLField()
    item_urls = models.URLField()

    def __str__(self):
        return self.name
