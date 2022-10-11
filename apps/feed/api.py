import json
import re

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from apps.notification.utilities import create_notification

from apps.feed.models import Tweek, Like


@login_required
def api_add_tweek(request):
    data = json.loads(request.body)
    body = data['body']

    tweek = Tweek.objects.create(body=body, created_by=request.user)

    results = re.findall("(^|[^@\w])@(\w{1,20})", body)

    for result in results:
        result = result[1]

        print(result)

        if User.objects.filter(username=result).exists() and result != request.user.username:
            user = User.objects.get(username=result)
            create_notification(request, user, 'mention')

    return JsonResponse({'id': tweek.id, 'success': True})

@login_required
def api_add_like(request):
    data = json.loads(request.body)
    tweek_id = data['tweek_id']

    if not Like.objects.filter(tweek_id=tweek_id).filter(created_by=request.user).exists():
        like = Like.objects.create(tweek_id=tweek_id, created_by=request.user)
        tweek = Tweek.objects.get(pk=tweek_id)
        if request.user != tweek.created_by:
            create_notification(request, tweek.created_by, 'like')

    return JsonResponse({'success': True})

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