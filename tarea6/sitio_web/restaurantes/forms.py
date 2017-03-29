from django import forms

from .models import *

from lxml import etree

class RestaurantForm(forms.Form):
    name    = forms.CharField(required=True, label='Nombre', max_length=80, widget=forms.TextInput(attrs={'placeholder': 'Pizzería Romana'}))
    city    = forms.CharField(required=True, label='Ciudad', widget=forms.TextInput(attrs={'placeholder': 'Granada'}))
    cuisine = forms.CharField(required=True, label='Tipo de cocina', widget=forms.TextInput(attrs={'placeholder': 'Italiana'}))
    borough = forms.CharField(required=True, label='Barrio', widget=forms.TextInput(attrs={'placeholder': 'La Chana'}))
    photo   = forms.FileField(required=False, label='Foto')

    def save(self, commit=True):
        api_base_url = 'http://maps.googleapis.com/maps/api/geocode/xml?address='
        req = api_base_url + self.cleaned_data['name'] + self.cleaned_data['city']

        tree = etree.parse(req)

        addressXML = tree.xpath('//address_component')
        locationXML = tree.xpath('//location')

        buildingXML = addressXML[0].xpath('//long_name/text()')[0]
        streetXML = addressXML[1].xpath('//long_name/text()')[1]
        cityXML = addressXML[2].xpath('//long_name/text()')[2]
        zipcodeXML = int(addressXML[6].xpath('//long_name/text()')[6])
        coordXML = [float(locationXML[0].xpath('//lat/text()')[0]), float(locationXML[0].xpath('//lng/text()')[0])]

        a = addr(building=buildingXML, street=streetXML, city=cityXML, zipcode=zipcodeXML, coord=coordXML)

        r = restaurants()

        r.name = self.cleaned_data['name']
        r.restaurant_id = restaurants.objects.count() + 1
        r.cuisine = self.cleaned_data['cuisine']
        r.borough = self.cleaned_data['borough']
        r.address = a

        if self.cleaned_data['photo']:
            restaurant_photo = open('static/img/restaurants/' + str(restaurants.objects.count() + 1) + '.jpg', 'rb')
            r.photo.put(restaurant_photo, content_type = 'image/jpeg')

        if commit:
            r.save()

        return r
