from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
import re
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from apps.notification.utilities import create_notification
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import TweekSerializer
from apps.feed.models import Tweek, Like, Dislike


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
def view_tweek(request, tweek_id):
    tweek = Tweek.objects.get(id=tweek_id)
    return render(request, 'tweek.html', {'tweek': tweek})


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


@login_required
@csrf_exempt
def api_add_tweek(request):
    data = json.loads(request.body)
    body = data['body']
    retweek_id = data['retweek_id']
    tweek = Tweek.objects.create(body=body, created_by=request.user, retweek_id=retweek_id)
    results = re.findall("(^|[^@\w])@(\w{1,20})", body)
    for result in results:
        result = result[1]
        if User.objects.filter(username=result).exists() and result != request.user.username:
            user = User.objects.get(username=result)
            create_notification(request, user, 'mention')
    return JsonResponse({'success': True})


def check_user_exists(username):
    try:
        User.objects.get(username=username)
        return True
    except User.DoesNotExist:
        return False


@login_required
@csrf_exempt
def api_add_like(request):
    data = json.loads(request.body)
    tweek_id = data['tweek_id']
    tweek = Tweek.objects.get(id=tweek_id)

    if tweek.retweek:
        Like.objects.create(tweek_id=tweek.retweek.id, created_by=request.user)
    else:
        Like.objects.create(tweek_id=tweek.id, created_by=request.user)

    if request.user != tweek.created_by:
        create_notification(request.user, tweek.created_by, 'like')

    return JsonResponse({'success': True})


@login_required
@csrf_exempt
def api_remove_like(request):
    data = json.loads(request.body)
    tweek_id = data['tweek_id']
    tweek = Tweek.objects.get(id=tweek_id)

    if tweek.retweek:
        if Like.objects.filter(tweek_id=tweek.retweek.id).filter(created_by=request.user).exists():
            Like.objects.get(tweek_id=tweek.retweek.id, created_by=request.user).delete()
    elif Like.objects.filter(tweek_id=tweek.id).filter(created_by=request.user).exists():
        Like.objects.get(tweek_id=tweek.id, created_by=request.user).delete()

    return JsonResponse({'success': True})


@login_required
@csrf_exempt
def api_add_dislike(request):
    data = json.loads(request.body)
    tweek_id = data['tweek_id']
    tweek = Tweek.objects.get(id=tweek_id)

    if tweek.retweek:
        Dislike.objects.create(tweek_id=tweek.retweek.id, created_by=request.user)
    else:
        Dislike.objects.create(tweek_id=tweek.id, created_by=request.user)

    if request.user != tweek.created_by:
        create_notification(request.user, tweek.created_by, 'dislike')

    return JsonResponse({'success': True})


@login_required
@csrf_exempt
def api_remove_dislike(request):
    data = json.loads(request.body)
    tweek_id = data['tweek_id']
    tweek = Tweek.objects.get(id=tweek_id)

    if tweek.retweek:
        if Dislike.objects.filter(tweek_id=tweek.retweek.id).filter(created_by=request.user).exists():
            Dislike.objects.get(tweek_id=tweek.retweek.id, created_by=request.user).delete()
    elif Dislike.objects.filter(tweek_id=tweek_id).filter(created_by=request.user).exists():
        Dislike.objects.get(tweek_id=tweek_id, created_by=request.user).delete()

    return JsonResponse({'success': True})


@login_required
@csrf_exempt
def api_remove_retweek(request):
    data = json.loads(request.body)
    tweek_id = data['tweek_id']
    if Tweek.objects.filter(retweek_id=tweek_id).filter(created_by=request.user).exists():
        tweek = Tweek.objects.get(retweek_id=tweek_id, created_by=request.user)
        tweek.delete()

    return JsonResponse({'success': True})


@login_required
@csrf_exempt
def api_delete_tweek(request):
    data = json.loads(request.body)
    tweek_id = data['tweek_id']

    tweek = Tweek.objects.get(pk=tweek_id)

    if tweek.created_by == request.user:
        tweek.delete()

    return JsonResponse({'success': True})


@login_required
@csrf_exempt
@api_view(['GET'])
def api_get_tweeks(request):
    userids = [request.user.id]
    for tweeker in request.user.twikkerprofile.follows.all():
        userids.append(tweeker.user.id)
    tweeks = Tweek.objects.filter(created_by__id__in=userids)
    paginator = PageNumberPagination()
    paginator.page_size = 20
    results = paginator.paginate_queryset(tweeks, request)
    serializer = TweekSerializer(results, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@login_required
@csrf_exempt
@api_view(['GET'])
def api_get_profile_tweeks(request, user_id):
    tweeks = Tweek.objects.filter(created_by=user_id)
    paginator = PageNumberPagination()
    paginator.page_size = 20
    results = paginator.paginate_queryset(tweeks, request)
    serializer = TweekSerializer(results, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@login_required
@csrf_exempt
@api_view(['GET'])
def api_get_tweek(request, tweek_id):
    tweek = Tweek.objects.get(id=tweek_id)
    serializer = TweekSerializer(tweek, many=False, context={'request': request})
    return JsonResponse({'success': True, 'tweek': serializer.data})