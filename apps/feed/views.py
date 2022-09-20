from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Tweek

@login_required
def feed(request):
    userids = [request.user.id]

    for tweeker in request.user.twikkerprofile.follows.all():
        userids.append(tweeker.user.id)

    tweeks = Tweek.objects.filter(created_by__id__in=userids).order_by('-created_at')

    return render(request, 'feed.html', {'tweeks': tweeks})

@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        tweekers = User.objects.filter(username__icontains=query)
    else:
        tweekers = []

    context = {
        'query': query,
        'tweekers': tweekers,
    }

    return render(request, 'search.html', context)