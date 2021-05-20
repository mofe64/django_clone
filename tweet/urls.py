from django.urls import path
from .views import get_home, delete_tweet

urlpatterns = [
    path('', get_home, name='home'),
    path('<int:tweet_id>', delete_tweet, name='delete_tweet')
]
