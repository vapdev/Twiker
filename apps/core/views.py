from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404


def frontpage(request):
    return render(request, 'core/frontpage.html')


def users(request):
    profiles = [user.twikkerprofile for user in User.objects.all()]


    context = {
        'users': profiles,
    }

    return render(request, 'core/users.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})