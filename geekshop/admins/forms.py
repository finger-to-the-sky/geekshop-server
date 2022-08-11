from django import forms
from django.forms import ModelForm

from users.forms import UserRegistationForm, UserProfileForm
from users.models import User
from products.models import ProductCategory


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