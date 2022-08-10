from django.urls import path

from admins.views import index, admins_users, admin_users_create, admin_users_update

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admins_users, name='admins_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
    path('users-update/<int:pk>/', admin_users_update, name='admin_users_update'),
]