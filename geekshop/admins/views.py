from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from admins.forms import UserAdminRegistrationFrom
from users.models import User


def index(request):
    context = {
        'title': 'GeekShop - Admin'
    }
    return render(request, 'admins/index.html', context)



# Read Controller
def admins_users(request):
    users = User.objects.all()

    context = {
        'title': 'GeekShop - Admin',
        'users': users,
    }
    return render(request, 'admins/admin-users-read.html', context)

def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationFrom(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно создан!')
            return HttpResponseRedirect(reverse('admins_staff:admins_users'))

    else:
        form = UserAdminRegistrationFrom()
    context = {'title': 'Создание пользователя', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)