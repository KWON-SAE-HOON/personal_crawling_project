from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path('create/', views.create, name='create'),
    
    path('', views.index, name='index'),

    path('<int:posting_pk>/', views.detail, name='detail'),
   
    path('<int:posting_pk>/delete/', views.delete, name='delete'),
    
    path('<int:posting_pk>/update/', views.update, name='update'),
    
    
    path('<int:posting_pk>/replies/create/', views.create_reply, name='create_reply'),

    path('<int:posting_pk>/replies/<int:reply_pk>/delete/', views.delete_reply, name='delete_reply'),
]