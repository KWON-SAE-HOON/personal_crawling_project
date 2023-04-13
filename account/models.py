from django.db import models
from django.contrib.auth.models import AbstractUser
from community.models import Posting

class SteamUser(models.Model):
    steam_id = models.CharField(max_length=17)
    name = models.CharField(max_length=200)
    profile_url = models.URLField()
    avatar_url = models.URLField()
    item_urls = models.URLField()

    
class TradeUser(AbstractUser):
     trade_request = models.ManyToManyField(Posting, related_name='trade_request')
     steam_url = models.CharField(max_length=17 , default='17자리 숫자를 입력해 주세요')
