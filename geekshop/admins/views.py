from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from admins.forms import UserAdminRegistrationFrom, UserAdminProfileFrom
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
    context = {'title': 'Создание пользователя', 'form': form, }
    return render(request, 'admins/admin-users-create.html', context)

# Update controller
def admin_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileFrom(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь отредактирован!')
            return HttpResponseRedirect(reverse('admins_staff:admins_users'))

    else:
        form = UserAdminProfileFrom(instance=selected_user)

    context = {
        'title': 'GeekShop - Admin',
        'form': form,
        'selected_user': selected_user

    }
    return render(request, 'admins/admin-users-update-delete.html', context)


def admin_users_delete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    messages.success(request, 'Пользователь удален!')
    return HttpResponseRedirect(reverse('admins_staff:admins_users'))