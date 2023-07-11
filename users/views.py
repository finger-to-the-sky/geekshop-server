from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegistationForm, UserProfileForm
from baskets.models import Basket


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
            messages.success(request, 'Поздравляем! Регистрация прошла успешно.')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistationForm()
    context = {
        'title': 'GeekShop - Регистрация', 'form': form}

    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(instance=user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сохранено')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)

    context = {
        'title': 'GeekShop - Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=user),
    }

    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
