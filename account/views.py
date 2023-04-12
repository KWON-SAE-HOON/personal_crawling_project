from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from . models import SteamUser, TradeUser
from . forms import TradeUserForm
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


@require_http_methods(['GET','POST'])
def signup(request):
    
    if request.method == 'POST':
        form = TradeUserForm(request.POST)
        if form.is_valid():
            user = form.save() # 새로 생성된 사용자
            login(request, user) # 새로 생성된 사용자로 로그인(set cookie)
            return redirect('community:index')
        
    else:
        form = TradeUserForm()
    return render(request, 'accounts/signup.html',{
        'form' : form,
    })

@require_http_methods(['GET','POST'])
def signin(request):
  
    if request.user.is_authenticated:
      
        return redirect('community:index')
    
    if request.method == 'POST':
        #                           ID/PW
        form = AuthenticationForm(request, request.POST)
     
        if form.is_valid():
            
            user = form.get_user()  
            login(request, user) 
         
            return redirect(request.GET.get('next') or 'community:index')
        
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html',{
        'form' : form,
    })

def signout(request):
    logout(request)
    return redirect('community:index')