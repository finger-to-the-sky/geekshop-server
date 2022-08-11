from django.urls import path

from admins.views import AdminUsers, index, AdminCategories

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', AdminUsers.admins_users, name='admins_users'),
    path('users-create/', AdminUsers.admin_users_create, name='admin_users_create'),
    path('users-update/<int:pk>/', AdminUsers.admin_users_update, name='admin_users_update'),
    path('users-delete/<int:pk>/', AdminUsers.admin_users_delete, name='admin_users_delete'),
    path('categories/', AdminCategories.admins_categories, name='admins_categories'),
    path('categories-create/', AdminCategories.admin_categories_create, name='admin_categories_create'),
    path('categories-update/<int:pk>/', AdminCategories.admin_categories_update, name='admin_categories_update'),
    path('categories-delete/<int:pk>/', AdminCategories.admin_categories_delete, name='admin_categories_delete'),
]