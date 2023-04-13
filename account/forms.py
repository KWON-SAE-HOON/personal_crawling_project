from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

TradeUser = get_user_model()


class TradeUserForm(UserCreationForm):
    class Meta:
        model = TradeUser
        fields = ('steam_url','username',)