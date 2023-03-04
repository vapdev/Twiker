from django.shortcuts import render
import json
import re
from django.db.models import Count
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from apps.notification.utilities import create_notification, create_notification_bulk
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from cloudinary import uploader
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from ..notification.models import Notification
from .serializers import TweekSerializer
from apps.feed.models import Tweek, Like, Dislike



@permission_classes((IsAuthenticated, ))
def view_tweek(request, tweek_id):
    tweek = Tweek.objects.get(id=tweek_id)
    return render(request, 'tweek.html', {'tweek': tweek})


@permission_classes((IsAuthenticated, ))
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


@permission_classes((IsAuthenticated, ))
@csrf_exempt
@api_view(['POST'])
def api_add_tweek(request):
    body = request.POST.get('body', '')
    parent_id = request.POST.get('parent_id', None)
    tweek_type = request.POST.get('tweek_type', None)
    user = request.user
    # process image
    image = request.FILES.get('image', None)
    if image:
        result = uploader.upload(image, upload_preset="ml_default")
        image_url = result['secure_url']
    else:
        image_url = None

    if tweek_type == 'retweek':
        Tweek.objects.create(body=body, created_by=user, retweek_id=parent_id, image=image_url)

    elif tweek_type == 'reply':
        Tweek.objects.create(body=body, created_by=user, comment_from_id=parent_id, image=image_url)
    else:
        Tweek.objects.create(body=body, created_by=user, image=image_url)

    # send notification to users mentioned in the tweek
    results = re.findall("(^|[^@\w])@(\w{1,20})", body)
    notifications = []
    for result in results:
        result = result[1]
        if User.objects.filter(username=result).exists() and result != request.user.username:
            user = User.objects.get(username=result)
            notification = Notification(created_by=request, to_user=user, notification_type='mention')
            notifications.append(notification)
    create_notification_bulk(notifications)

    return JsonResponse({'success': True})


@permission_classes((IsAuthenticated, ))
@csrf_exempt
@api_view(['POST'])
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


@permission_classes((IsAuthenticated, ))
@csrf_exempt
@api_view(['POST'])
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


@permission_classes((IsAuthenticated, ))
@csrf_exempt
@api_view(['POST'])
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


@permission_classes((IsAuthenticated, ))
@csrf_exempt
@api_view(['POST'])
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


@permission_classes((IsAuthenticated, ))
@csrf_exempt
@api_view(['POST'])
def api_remove_retweek(request):
    data = json.loads(request.body)
    tweek_id = data['tweek_id']
    if Tweek.objects.filter(retweek_id=tweek_id).filter(created_by=request.user).exists():
        tweek = Tweek.objects.get(retweek_id=tweek_id, created_by=request.user)
        tweek.delete()

    return JsonResponse({'success': True})


@permission_classes((IsAuthenticated, ))
@csrf_exempt
@api_view(['POST'])
def api_delete_tweek(request):
    data = json.loads(request.body)
    tweek_id = data['tweek_id']
    print("tweek id is")

    tweek = Tweek.objects.get(pk=tweek_id)

    if tweek.created_by == request.user:
        tweek.delete()

    return JsonResponse({'success': True})


@permission_classes((IsAuthenticated, ))
@csrf_exempt
@api_view(['GET'])
def api_get_tweeks(request):
    userids = [request.user.id]
    for tweeker in request.user.twikkerprofile.follows.all():
        userids.append(tweeker.user.id)
    tweeks = Tweek.objects.filter(created_by__id__in=userids)
    if request.GET.get('order_by') == '0':
        tweeks = tweeks.order_by('-created_at')
    elif request.GET.get('order_by') == '1':
        tweeks = tweeks.order_by('-likes')
    elif request.GET.get('order_by') == '2':
        print(request.GET.get('order_by'))
        tweeks = tweeks.annotate(num_retweets=Count('retweek')).order_by('-num_retweets')
    paginator = PageNumberPagination()
    paginator.page_size = 25
    print("ui")
    results = paginator.paginate_queryset(tweeks, request)
    serializer = TweekSerializer(results, many=True, context={'request': request})
    print(serializer.data)
    return paginator.get_paginated_response(serializer.data)


@permission_classes((IsAuthenticated, ))
@csrf_exempt
@api_view(['GET'])
def api_get_profile_tweeks(request, user_id):
    tweeks = Tweek.objects.filter(created_by=user_id)
    paginator = PageNumberPagination()
    paginator.page_size = 25
    results = paginator.paginate_queryset(tweeks, request)
    serializer = TweekSerializer(results, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@permission_classes((IsAuthenticated, ))
@csrf_exempt
@api_view(['GET'])
def api_get_reply_tweeks(request, tweek_id):
    tweeks = Tweek.objects.filter(comment_from_id=tweek_id)
    serializer = TweekSerializer(tweeks, many=True, context={'request': request})
    return JsonResponse({'success': True, 'tweeks': serializer.data})


@permission_classes((IsAuthenticated, ))
@csrf_exempt
@api_view(['GET'])
def api_get_tweek(request, tweek_id):
    tweek = Tweek.objects.get(id=tweek_id)
    serializer = TweekSerializer(tweek, many=False, context={'request': request})
    return JsonResponse({'success': True, 'tweek': serializer.data})
