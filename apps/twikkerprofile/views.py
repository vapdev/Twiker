from asgiref.sync import sync_to_async
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from apps.notification.utilities import create_notification

from .forms import TwikkerProfileForm
from ..notification.models import Notification


def twikkerprofile(request, username):
    user = get_object_or_404(User, username=username)
    tweeks = user.tweeks.all()

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

    context = {
        'user': user,
        'tweeks': tweeks,
    }

    return render(request, 'twikkerprofile/twikkerprofile.html', context)


@permission_classes((IsAuthenticated, ))
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


@sync_to_async
def save_follow(follower_id, following_id):
    follower = User.objects.get(id=follower_id)
    following = User.objects.get(id=following_id)
    follower.twikkerprofile.follows.add(following.twikkerprofile)
    create_notification(created_by=follower, notification_type=Notification.FOLLOWER, to_user=following)


@permission_classes((IsAuthenticated, ))
def unfollow_tweeker(request, username):
    user = get_object_or_404(User, username=username)

    request.user.twikkerprofile.follows.remove(user.twikkerprofile)

    return redirect('twikkerprofile', username=username)


@permission_classes((IsAuthenticated, ))
def follow_tweeker(request, username):
    user = get_object_or_404(User, username=username)

    request.user.twikkerprofile.follows.add(user.twikkerprofile)

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


@permission_classes((IsAuthenticated, ))
@api_view(['POST'])
def toggle_dark_mode(request):
    data = request.data
    user_id = data['user_id']
    user = User.objects.get(id=user_id)
    user.twikkerprofile.dark_mode = not user.twikkerprofile.dark_mode
    print("Dark mode: ", user.twikkerprofile.dark_mode)
    user.twikkerprofile.save()
    return JsonResponse({'dark_mode': user.twikkerprofile.dark_mode})