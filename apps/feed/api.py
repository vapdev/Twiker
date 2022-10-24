import json
import re

from asgiref.sync import sync_to_async
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from apps.notification.models import Notification
from apps.notification.utilities import create_notification

from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from .serializers import TweekSerializer
from apps.feed.models import Tweek, Like

@sync_to_async
def save_tweek(body, tweeker):
    tweeker = User.objects.get(username=tweeker)
    Tweek.objects.create(body=body, created_by=tweeker)

    results = re.findall("(^|[^@\w])@(\w{1,20})", body)
    results = [result[1] for result in results]

    for result in results:
        if check_user_exists(username=result):
            if result != tweeker:
                user = User.objects.get(username=result)
                tweeker = User.objects.get(username=tweeker)
                create_notification(created_by=tweeker, notification_type=Notification.MENTION, to_user=user)

def check_user_exists(username):
    try:
        User.objects.get(username=username)
        return True
    except User.DoesNotExist:
        return False
@sync_to_async
def save_like(tweek_id, liker):
    tweek = Tweek.objects.get(id=tweek_id)
    liker = User.objects.get(username=liker)
    Like.objects.create(tweek_id=tweek_id, created_by=liker)
    tweek.save()

    if tweek.created_by != liker:
        create_notification(created_by=liker, notification_type=Notification.LIKE, to_user=tweek.created_by)

@login_required
def api_remove_like(request):
    data = json.loads(request.body)
    tweek_id = data['tweek_id']
    if Like.objects.filter(tweek_id=tweek_id).filter(created_by=request.user).exists():
        like = Like.objects.get(tweek_id=tweek_id, created_by=request.user)
        like.delete()

    return JsonResponse({'success': True})

@login_required
def api_delete_tweek(request):
    data = json.loads(request.body)
    tweek_id = data['tweek_id']

    tweek = Tweek.objects.get(pk=tweek_id)

    if tweek.created_by == request.user:
        tweek.delete()

    return JsonResponse({'success': True})

@login_required
@api_view(['GET'])
def api_get_tweeks(request):
    userids = [request.user.id]
    for tweeker in request.user.twikkerprofile.follows.all():
        userids.append(tweeker.user.id)
    tweeks = Tweek.objects.filter(created_by__id__in=userids)
    paginator = PageNumberPagination()
    paginator.page_size = 20
    results = paginator.paginate_queryset(tweeks, request)
    serializer = TweekSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)