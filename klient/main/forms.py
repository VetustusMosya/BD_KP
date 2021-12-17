from .models import *
from django.forms import ModelForm, TextInput, DateInput, Select, NumberInput
from django import forms


class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = ['customer', 'pickup_date', 'pickup_adress', 'delivery_adress', 'weight', 'type']

        widgets = {
            'customer': TextInput(attrs={
                'class': 'form__input',
                'placeholder': 'Цифра'
            }),
            'pickup_date': DateInput(attrs={
                'class': 'form__input',
                'placeholder': 'ГГГГ-ММ-ДД'
            }),
            'pickup_adress': TextInput(attrs={
                'class': 'form__input',
                'placeholder': ''
            }),
            'delivery_adress': TextInput(attrs={
                'class': 'form__input',
                'placeholder': "'---' если доставка "
            }),
            'weight': NumberInput(attrs={
                'class': 'form__input'
            }),
        }
