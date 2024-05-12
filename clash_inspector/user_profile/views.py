from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect, redirect

from .forms import UserRegisterForm, UserLoginForm
from .models import UserProfile


def user_profile(request):
    profile = UserProfile.objects.all()
    context: dict = {
        'user_profile': profile,
    }
    return render(request, 'user_profile/profile.html', context)


def register_page(request):
    form = UserRegisterForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('search'))

    return render(request, 'user_profile/register_page.html', context)


def login_page(request):
    form = UserLoginForm(request=request)
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)

                return HttpResponseRedirect(reverse('search'))

    context = {'form': form}
    return render(request, 'user_profile/login_page.html', context)


def log_out(request):
    logout(request)
    return redirect('search')
