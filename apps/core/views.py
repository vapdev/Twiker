from django.contrib.auth import login
from rest_framework import generics

from .forms import CustomUserForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .serializers import UserSerializer


def users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'core/users.html', context)


class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'core/signup.html', {'form':form})
    else:
        form = CustomUserForm()
    return render(request, 'core/signup.html', {'form': form})

