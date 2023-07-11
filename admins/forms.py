from django import forms
from django.forms import ModelForm

from users.forms import UserRegistationForm, UserProfileForm
from users.models import User
from products.models import ProductCategory, Product


class UserAdminRegistrationFrom(UserRegistationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input', }), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email', 'password1', 'password2', 'age')



class UserAdminProfileFrom(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'readonly': False
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'readonly': False
    }))


class CategoriesAdminForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'readonly': False
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'readonly': False
    }))
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')


class ProductsAdminForm(ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Название продукта'}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Описание'}))
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), empty_label='Выберите категорию')
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Цена'}),
                             required=False)
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Количество'}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)


    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'quantity', 'image')