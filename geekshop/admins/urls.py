from django.urls import path

from admins.views import index, UserAdminListView, UserAdminCreateView, UserAdminUpdateView, UserAdminDeleteView, \
    CategoryAdminListView, CategoryAdminCreateView, CategoryAdminUpdateView, CategoryAdminDeleteView, \
    ProductAdminListView, ProductAdminCreateView, ProductAdminUpdateView, ProductAdminDeleteView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users-admin/', UserAdminListView.as_view(), name='admin_users'),
    path('users-create/', UserAdminCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', UserAdminUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', UserAdminDeleteView.as_view(), name='admin_users_delete'),

    path('categories/', CategoryAdminListView.as_view(), name='admin_categories'),
    path('categories-create/', CategoryAdminCreateView.as_view(), name='admin_categories_create'),
    path('categories-update/<int:pk>/', CategoryAdminUpdateView.as_view(), name='admin_categories_update'),
    path('categories-delete/<int:pk>/', CategoryAdminDeleteView.as_view(), name='admin_categories_delete'),

    path('products-admin/', ProductAdminListView.as_view(), name='admin_products'),
    path('products-create/', ProductAdminCreateView.as_view(), name='admin_products_create'),
    path('products-update/<int:pk>/', ProductAdminUpdateView.as_view(), name='admin_products_update'),
    path('products-delete/<int:pk>/', ProductAdminDeleteView.as_view(), name='admin_products_delete'),
]