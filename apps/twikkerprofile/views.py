from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from apps.notification.utilities import create_notification

from .forms import TwikkerProfileForm

def twikkerprofile(request, username):
    user = get_object_or_404(User, username=username)
    tweeks = user.tweeks.all()

    for tweek in tweeks:
        likes = tweek.likes.filter(created_by__id=request.user.id)

        if likes.count() > 0:
            tweek.liked = True
        else:
            tweek.liked = False

    context = {
        'user': user,
        'tweeks': tweeks,
    }

    return render(request, 'twikkerprofile/twikkerprofile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = TwikkerProfileForm(request.POST, request.FILES, instance=request.user.twikkerprofile)
        if form.is_valid():
            form.save()
            return redirect('twikkerprofile', username=request.user.username)
    else:
        form = TwikkerProfileForm(instance=request.user.twikkerprofile)

    context = {
        'user': request.user,
        'form': form,
    }

    return render(request, 'twikkerprofile/edit_profile.html', context)


@login_required
def follow_tweeker(request, username):
    user = get_object_or_404(User, username=username)

    request.user.twikkerprofile.follows.add(user.twikkerprofile)

    if request.user != user:
        create_notification(request, user, 'follower')

    return redirect('twikkerprofile', username=username)


@login_required
def unfollow_tweeker(request, username):
    user = get_object_or_404(User, username=username)

    request.user.twikkerprofile.follows.remove(user.twikkerprofile)

    return redirect('twikkerprofile', username=username)

def followers(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user,
        'followers': user.twikkerprofile.follows.all(),
    }

    return render(request, 'twikkerprofile/followers.html', context)

def follows(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user,
        'follows': user.twikkerprofile.followed_by.all(),
    }

    return render(request, 'twikkerprofile/follows.html', context)