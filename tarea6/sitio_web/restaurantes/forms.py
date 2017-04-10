from django import forms

from .models import *

class RestaurantForm(forms.Form):
    name    = forms.CharField(required=True, label='Nombre', max_length=80, widget=forms.TextInput(attrs={'placeholder': 'Pizzería Romana'}))
    city    = forms.CharField(required=True, label='Ciudad', widget=forms.TextInput(attrs={'placeholder': 'Granada'}))
    cuisine = forms.CharField(required=True, label='Tipo de cocina', widget=forms.TextInput(attrs={'placeholder': 'Italiana'}))
    borough = forms.CharField(required=True, label='Barrio', widget=forms.TextInput(attrs={'placeholder': 'La Chana'}))
    photo   = forms.ImageField(required=False, label='Foto')
