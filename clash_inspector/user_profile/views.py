from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse


def user_profile(request):
    user = User()
    context = {
        'user': user
    }
    return render(request, 'user_profile/home.html', context)


def register_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        player_tag = request.POST['player_tag']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            error_message = 'Passwords do not match'
            return render(request, 'user_profile/register_page.html', {'error_message': error_message})

        else:
            print('pass corected')
            if User.objects.filter(username=username).exists():
                print('User exist')
                error_message = 'User already exsist'
                return render(request, 'user_profile/register_page.html', {'error_message': error_message})
            else:
                User.objects.filter(username=username).exists()
                user = User.objects.create_user(username=username, password=password2)
                user.save()
                return HttpResponseRedirect(reverse('login_page'))

    return render(request, 'user_profile/register_page.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(redirect_to=reverse('profile'))
        else:
            error = 'Incorect login or password'
            context: dict = {
                'error': error
            }
            return render(request, 'user_profile/login_page.html', context)

    return render(request, 'user_profile/login_page.html')


def log_out(request):
    logout(request)
    return redirect('search')
