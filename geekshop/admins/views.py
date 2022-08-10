from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from admins.forms import UserAdminRegistrationFrom, UserAdminProfileFrom
from users.models import User

@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {
        'title': 'GeekShop - Admin'
    }
    return render(request, 'admins/index.html', context)



# Read Controller
@user_passes_test(lambda u: u.is_staff)
def admins_users(request):
    users = User.objects.all()

    context = {
        'title': 'GeekShop - Admin',
        'users': users,
    }
    return render(request, 'admins/admin-users-read.html', context)


# Create Controller
@user_passes_test(lambda u: u.is_staff)
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
@user_passes_test(lambda u: u.is_staff)
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


# Delete Controller
@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, pk):
    user = User.objects.get(id=pk)
    user.save_delete()
    messages.success(request, 'Пользователь деактивирован!')
    return HttpResponseRedirect(reverse('admins_staff:admins_users'))