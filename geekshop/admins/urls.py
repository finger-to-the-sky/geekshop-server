from django.urls import path

from admins.views import index, admins_users, admin_users_create

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admins_users, name='admins_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
]