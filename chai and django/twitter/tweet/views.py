from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import redirect, get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweet = Tweet.objects.all().order_by('-created_at')

    return render(request, 'tweet_list.html', {'tweet':tweet})

def tweet_create(request):
    if request.method == 'POST':
        tweet = TweetForm(request.POST, request.FILES)
        if tweet.is_valid():
            tweet.save(commit=False)
            tweet.user = request.user
            tweet.save()

            redirect('tweet_list')
    else:
        form = TweetForm()

    return render(request, 'tweet_create.html', {'form':form})

def tweet_update(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_create.html', {'form':form})

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
    else:
        return render(request, 'tweet_confirm_delete.html')


