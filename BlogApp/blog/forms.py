from django import forms
from .models import Users
from django.forms import ModelForm, TextInput, DateTimeInput


class UsersForm(ModelForm):

    class Meta:
        model = Users
        fields = ['name', 'second_name', 'email', 'city', 'pol', 'date']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "second_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш e-mail адрес:'
            }),
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
            "pol": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш пол'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата регистрации'
            })
        }