from django.urls import path
from django.contrib.auth import views
from apps.core.views import frontpage, signup, users, UsersList

urlpatterns = [
    path('cornelios/', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('users/', users, name='users'),
    path('api/users/', UsersList.as_view(), name='api_get_users'),
]