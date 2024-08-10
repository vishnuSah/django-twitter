
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweetlist/', views.tweet_list, name='tweet_list'),
] 
