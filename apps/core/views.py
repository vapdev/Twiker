from django.contrib.auth import login
from .forms import CustomUserForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404


def frontpage(request):
    return render(request, 'core/frontpage.html')


def users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'core/users.html', context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
        else:
            return render(request, 'core/signup.html', {'form':form})
    else:
        form = CustomUserForm()
    return render(request, 'core/signup.html', {'form': form})

