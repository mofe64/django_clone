from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet
from .forms import TweetForm


# Create your views here.

def get_home(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    all_tweets = Tweet.objects.all()
    form = TweetForm()
    context = {
        'tweets': all_tweets,
        'form': form
    }
    return render(request, 'index.html', context)


def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    tweet.delete()
    return redirect('home')
