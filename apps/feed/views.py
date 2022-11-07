import json

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Tweek

@login_required
def feed(request):
    userids = [request.user.id]

    for tweeker in request.user.twikkerprofile.follows.all():
        userids.append(tweeker.user.id)

    tweeks = Tweek.objects.filter(created_by__id__in=userids)

    for tweek in tweeks:
        likes = tweek.likes.filter(created_by__id=request.user.id)

        if likes.count() > 0:
            tweek.liked = True
        else:
            tweek.liked = False

        dislikes = tweek.dislikes.filter(created_by__id=request.user.id)

        if dislikes.count() > 0:
            tweek.disliked = True
        else:
            tweek.disliked = False

    retweeked_tweeks_ids = [tweek.retweek.id for tweek in tweeks if tweek.retweek]

    return render(request, 'feed.html', {'tweeks': tweeks, 'retweeked_tweeks': retweeked_tweeks_ids})

@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        tweekers = User.objects.filter(username__icontains=query)
        tweeks = Tweek.objects.filter(body__icontains=query)
    else:
        tweekers = []
        tweeks = []

    context = {
        'query': query,
        'tweekers': tweekers,
        'tweeks': tweeks,
    }

    return render(request, 'search.html', context)

