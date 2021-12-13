from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, Select
from django import forms


class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = ['customer', 'pickup_date', 'pickup_adress', 'weight', 'type']

        widgets = {
            'customer': TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Цифра'
            }),
            'pickup_date': DateTimeInput(attrs={
                'class': 'form__input',
                'placeholder': 'ГГГГ-ММ-ДД'
            }),
            'pickup_adress': TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Адресс'
            }),
            'weight': TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Тонны'
            }),
        }

        class DeliveryForm(ModelForm):
            class Meta:
                model = Cargo
                fields = ['customer', 'pickup_date', 'pickup_adress', 'weight', 'type']

                widgets = {
                    'customer': TextInput(attrs={
                        'class': 'form__input',
                        'placeholder': 'Цифра'
                    }),
                    'pickup_date': DateTimeInput(attrs={
                        'class': 'form__input',
                        'placeholder': 'ГГГГ-ММ-ДД'
                    }),
                    'pickup_adress': TextInput(attrs={
                        'class': 'form__input',
                        'placeholder': 'Адресс'
                    }),
                    'weight': TextInput(attrs={
                        'class': 'form__input',
                        'placeholder': 'Тонны'
                    }),
                }

