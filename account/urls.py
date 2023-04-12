from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("<str:steam_id>/", views.get_steam_user_info, name="get_steam_user_info"),

    
]