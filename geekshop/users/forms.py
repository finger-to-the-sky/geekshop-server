from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import User

class UserLoginFrom(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя',
        'class': 'form-control py-4'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль',
        'class': 'form-control py-4'}))

    class Meta:
        model = User
        fields = ('username', 'password')
