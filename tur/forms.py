__author__ = 'Alejandro'

# -*- coding: utf-8 -*-
from .models import cuenta
from django.forms import ModelForm, SelectDateWidget
from django import forms

class cuentaFORM(forms.ModelForm):
    class Meta:
        model = cuenta
        fields = ('usuario','password')
        widgets = {
            'Usuario' : forms.TextInput(attrs={'class':'inputtext'}),
            'password': forms.PasswordInput(attrs={'': ''}),
        }