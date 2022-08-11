from django.urls import path

from admins.views import AdminUsers, index, AdminCategories, AdminProducts

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', AdminUsers.admin_users, name='admin_users'),
    path('users-create/', AdminUsers.admin_users_create, name='admin_users_create'),
    path('users-update/<int:pk>/', AdminUsers.admin_users_update, name='admin_users_update'),
    path('users-delete/<int:pk>/', AdminUsers.admin_users_delete, name='admin_users_delete'),

    path('categories/', AdminCategories.admin_categories, name='admin_categories'),
    path('categories-create/', AdminCategories.admin_categories_create, name='admin_categories_create'),
    path('categories-update/<int:pk>/', AdminCategories.admin_categories_update, name='admin_categories_update'),
    path('categories-delete/<int:pk>/', AdminCategories.admin_categories_delete, name='admin_categories_delete'),

    path('products/', AdminProducts.admin_products, name='admin_products'),
    path('products-create/', AdminProducts.admin_products_create, name='admin_products_create'),
    path('products-update/<int:pk>/', AdminProducts.admin_products_update, name='admin_products_update'),
    path('products-delete/<int:pk>/', AdminProducts.admin_products_delete, name='admin_products_delete'),
]