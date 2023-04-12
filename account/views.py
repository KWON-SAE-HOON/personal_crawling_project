from django.shortcuts import render
from django.http import HttpResponse
from .models import SteamUser
import requests
from bs4 import BeautifulSoup

def get_steam_user_info(request, steam_id):
    url = f"https://steamcommunity.com/profiles/{steam_id}"
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    name = soup.find("span", {"class": "actual_persona_name"}).text.strip()
    profile_url = url
    
    avatar_url = soup.find("div", {"class": "playerAvatarAutoSizeInner"}).img["src"]
    # 프로필 crawling
   
    user, created = SteamUser.objects.get_or_create(
        steam_id=steam_id,
        defaults={
            "name": name,
            "profile_url": profile_url,
            "avatar_url": avatar_url, 
           
        }
    )

    context = {
        "user": user,
    }

    return render(request, "account/user_info.html", context)

### 스팀 프로파일 크롤링
