from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


SteamUser = get_user_model()

class SteamUserForm(UserCreationForm):
    class Meta:
        model = SteamUser
        fields = ('steam_id', )
