from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from .forms import UserLoginForm, UserRegistationForm



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:

        form = UserLoginForm()
    context = {
        'title': 'GeekShop - Авторизация', 'form': form}

    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == "POST":
        form = UserRegistationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistationForm()
    context = {
        'title': 'GeekShop - Регистрация', 'form': form}

    return render(request, 'users/register.html', context)
