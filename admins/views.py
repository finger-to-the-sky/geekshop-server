from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin


from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from admins.forms import UserAdminRegistrationFrom, UserAdminProfileFrom, CategoriesAdminForm, ProductsAdminForm
from users.models import User
from products.models import ProductCategory, Product



@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {
        'title': 'GeekShop - Admin'
    }
    return render(request, 'admins/index.html', context)

class CommonMixin(SuccessMessageMixin):
    title = None

    def get_context_data(self, *args, **kwargs):
        context = super(CommonMixin, self).get_context_data(object_list=None, *args, **kwargs)
        context['title'] = self.title
        return context


class UserAdminListView(CommonMixin, ListView):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'GeekShop - Admin'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminListView, self).dispatch(request, *args, **kwargs)


class UserAdminCreateView(CommonMixin, CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegistrationFrom
    success_url = reverse_lazy('admins_staff:admin_users')
    success_message = 'Пользователь успешно создан!'


class UserAdminUpdateView(CommonMixin, UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileFrom
    success_url = reverse_lazy('admins_staff:admin_users')
    success_message = 'Пользователь успешно отредактирован!'


class UserAdminDeleteView(CommonMixin, DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins_staff:admin_users')
    success_message = 'Пользователь удален!'

class CategoryAdminListView(CommonMixin, ListView):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'
    title = 'Админка/Категории'


class CategoryAdminCreateView(CommonMixin, CreateView):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = CategoriesAdminForm
    success_url = reverse_lazy('admins_staff:admin_categories')
    title = 'Админка/Создание категории'
    success_message = 'Категория успешно создана!'


class CategoryAdminUpdateView(CommonMixin, UpdateView):
    model = ProductCategory
    form_class = CategoriesAdminForm
    template_name = 'admins/admin-categories-update-delete.html'
    success_url = reverse_lazy('admins_staff:admin_categories')
    title = 'Админка/Редактирование категории'
    success_message = 'Категория успешно изменёна!'


class CategoryAdminDeleteView(CommonMixin, DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    success_url = reverse_lazy('admins_staff:admin_categories')
    title = 'Админка/Редактирование пользователя'
    success_message = 'Товар удален!'


class ProductAdminListView(CommonMixin, ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'
    title = 'Админка/Продукты'


class ProductAdminCreateView(CommonMixin, CreateView):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductsAdminForm
    success_url = reverse_lazy('admins_staff:admin_products')
    title = 'Админка/Создание товара'
    success_message = 'Товар успешно создан!'


class ProductAdminUpdateView(CommonMixin, UpdateView):
    model = Product
    form_class = ProductsAdminForm
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins_staff:admin_products')
    title = 'Админка/Редактирование товара'
    success_message = 'Товар успешно изменён!'


class ProductAdminDeleteView(CommonMixin, DeleteView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins_staff:admin_products')
    title = 'Админка/Редактирование товара'
    success_message = 'Товар удален!'


# class AdminUsers:

    # # Read Controller
    # @user_passes_test(lambda u: u.is_staff)
    # def admin_users(request):
    #     users = User.objects.all()
    #     context = {'title': 'GeekShop - Admin', 'users': users,}
    #     return render(request, 'admins/admin-users-read.html', context)


    # Create Controller
    # @user_passes_test(lambda u: u.is_staff)
    # def admin_users_create(request):
    #     if request.method == 'POST':
    #         form = UserAdminRegistrationFrom(data=request.POST, files=request.FILES)
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, 'Пользователь успешно создан!')
    #             return HttpResponseRedirect(reverse('admins_staff:admin_users'))
    #
    #     else:
    #         form = UserAdminRegistrationFrom()
    #     context = {'title': 'Создание пользователя', 'form': form, }
    #     return render(request, 'admins/admin-users-create.html', context)

    # Update controller
    # @user_passes_test(lambda u: u.is_staff)
    # def admin_users_update(request, pk):
    #     selected_user = User.objects.get(id=pk)
    #     if request.method == 'POST':
    #         form = UserAdminProfileFrom(instance=selected_user, files=request.FILES, data=request.POST)
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, 'Пользователь отредактирован!')
    #             return HttpResponseRedirect(reverse('admins_staff:admin_users'))
    #
    #     else:
    #         form = UserAdminProfileFrom(instance=selected_user)
    #
    #     context = {
    #         'title': 'GeekShop - Admin',
    #         'form': form,
    #         'selected_user': selected_user
    #
    #     }
    #     return render(request, 'admins/admin-users-update-delete.html', context)


    # # Delete Controller
    # @user_passes_test(lambda u: u.is_staff)
    # def admin_users_delete(request, pk):
    #     user = User.objects.get(id=pk)
    #     user.save_delete()
    #     messages.success(request, 'Пользователь деактивирован!')
    #     return HttpResponseRedirect(reverse('admins_staff:admin_users'))

#
# class AdminCategories:
#
#     # Read Controller
#     @user_passes_test(lambda u: u.is_staff)
#     def admin_categories(request):
#         products_categories = ProductCategory.objects.all()
#
#         context = {
#             'title': 'GeekShop - Admin',
#             'products_categories': products_categories,
#         }
#         return render(request, 'admins/admin-categories-read.html', context)
#
#     # Create Controller
#     @user_passes_test(lambda u: u.is_staff)
#     def admin_categories_create(request):
#         if request.method == 'POST':
#             form = CategoriesAdminForm(data=request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Категория успешно создана!')
#                 return HttpResponseRedirect(reverse('admins_staff:admin_categories'))
#
#         else:
#             form = CategoriesAdminForm()
#         context = {'title': 'Создание категории', 'form': form, }
#         return render(request, 'admins/admin-categories-create.html', context)
#
#     # Update controller
#     @user_passes_test(lambda u: u.is_staff)
#     def admin_categories_update(request, pk):
#         selected_category = ProductCategory.objects.get(id=pk)
#         if request.method == 'POST':
#             form = CategoriesAdminForm(instance=selected_category, data=request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Категория отредактирована!')
#                 return HttpResponseRedirect(reverse('admins_staff:admin_categories'))
#
#         else:
#             form = CategoriesAdminForm(instance=selected_category)
#
#         context = {
#             'title': 'GeekShop - Admin',
#             'form': form,
#             'selected_category': selected_category
#
#         }
#         return render(request, 'admins/admin-categories-update-delete.html', context)
#
#     # Delete Controller
#     @user_passes_test(lambda u: u.is_staff)
#     def admin_categories_delete(request, pk):
#         products_categories = ProductCategory.objects.get(id=pk)
#         products_categories.safe_delete()
#         messages.success(request, 'Категория деактивирована!')
#         return HttpResponseRedirect(reverse('admins_staff:admin_categories'))
#
#
# class AdminProducts:
#
#     # Read Controller
#     @user_passes_test(lambda u: u.is_staff)
#     def admin_products(request):
#         admin_products = Product.objects.all()
#
#         context = {
#             'title': 'GeekShop - Admin',
#             'admin_products': admin_products,
#         }
#         return render(request, 'admins/admin-products-read.html', context)
#
#     # Create Controller
#     @user_passes_test(lambda u: u.is_staff)
#     def admin_products_create(request):
#         if request.method == 'POST':
#             form = ProductsAdminForm(data=request.POST, files=request.FILES)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Продукт успешно создан!')
#                 return HttpResponseRedirect(reverse('admins_staff:admin_products'))
#
#         else:
#             form = ProductsAdminForm()
#         context = {'title': 'Создание продукта', 'form': form, }
#         return render(request, 'admins/admin-products-create.html', context)
#
#     # Update controller
#     @user_passes_test(lambda u: u.is_staff)
#     def admin_products_update(request, pk):
#         selected_product = Product.objects.get(id=pk)
#         if request.method == 'POST':
#             form = ProductsAdminForm(instance=selected_product, files=request.FILES, data=request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Продукт отредактирован!')
#                 return HttpResponseRedirect(reverse('admins_staff:admin_products'))
#
#         else:
#             form = ProductsAdminForm(instance=selected_product)
#
#         context = {
#             'title': 'GeekShop - Admin',
#             'form': form,
#             'selected_product': selected_product
#
#         }
#         return render(request, 'admins/admin-products-update-delete.html', context)
#
#
#     # Delete Controller
#     @user_passes_test(lambda u: u.is_staff)
#     def admin_products_delete(request, pk):
#         admins_products = Product.objects.get(id=pk)
#         admins_products.safe_delete()
#         messages.success(request, 'Товар деактивирован!')
#         return HttpResponseRedirect(reverse('admins_staff:admin_products'))