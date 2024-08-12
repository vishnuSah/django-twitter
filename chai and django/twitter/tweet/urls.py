
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.tweet_list, name='tweet_list'),
    path('<int:tweet_id>/tweetedit', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/tweetdelete', views.tweet_delete, name='tweet_delete'),
] 
