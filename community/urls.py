from django.urls import path
from . import views

app_name = "steam_profile"

urlpatterns = [
    path('', views.index, name="index"),
    
    


   

]