from apps.feed.views import search, view_tweek #
from django.urls import path
from apps.feed.views import api_get_profile_tweeks, api_remove_like, api_delete_tweek, api_get_tweeks, api_remove_dislike, \
    api_remove_retweek, api_add_like, api_add_dislike, api_add_tweek, api_get_tweek
urlpatterns = [
    path('search/', search, name='search'),
    path('tweek/<int:tweek_id>/', view_tweek, name='view_tweek'),
    path('api/get_profile_tweeks/<int:user_id>/', api_get_profile_tweeks, name='get_profile_tweeks'),
    path('api/remove_like/', api_remove_like, name='remove_like'),
    path('api/delete_tweek/', api_delete_tweek, name='api_delete_tweek'),
    path('api/get_tweeks/', api_get_tweeks, name='get_tweeks'),
    path('api/remove_dislike/', api_remove_dislike, name='remove_dislike'),
    path('api/remove_retweek/', api_remove_retweek, name='remove_retweek'),
    path('api/add_like/', api_add_like, name='remove_like'),
    path('api/add_dislike/', api_add_dislike, name='remove_dislike'),
    path('api/add_tweek/', api_add_tweek, name='api_add_tweek'),
    path('api/tweek/<int:tweek_id>/', api_get_tweek, name='api_get_tweek'),

]