import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from apps.feed.models import Tweek


@login_required
def api_add_tweek(request):
    data = json.loads(request.body)
    body = data['body']

    tweek = Tweek.objects.create(body=body, created_by=request.user)

    return JsonResponse({'success': True})