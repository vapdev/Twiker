from django.contrib import admin

from .models import Tweek, Dislike, Like

admin.site.register(Tweek)
admin.site.register(Like)
admin.site.register(Dislike)