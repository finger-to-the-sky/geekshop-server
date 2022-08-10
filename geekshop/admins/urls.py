from django.urls import path

from admins.views import index, admins_users

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admins_users, name='admins_users'),
]