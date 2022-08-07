from django.shortcuts import render

from .forms import UserLoginFrom
def login(request):
    form = UserLoginFrom()

    context = {
        'title': 'GeekShop - Авторизация',
        'form' : form,
    }

    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'GeekShop - Регистрация'
    }

    return render(request, 'users/register.html', context)