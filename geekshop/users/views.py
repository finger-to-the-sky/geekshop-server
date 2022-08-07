from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from .forms import UserLoginFrom


def login(request):
    if request.method == 'POST':
        form = UserLoginFrom(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:

        form = UserLoginFrom()
    context = {
        'title': 'GeekShop - Авторизация', 'form': form}

    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'GeekShop - Регистрация', }

    return render(request, 'users/register.html', context)
