from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import restaurants, addr
from .forms import RestaurantForm

from lxml import etree

import datetime
import os.path
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - se ha consultado la página de inicio")
    return render(request, 'restaurantes/index.html')

def list(request):
    lista = restaurants.objects
    context = {
        "resta": lista,
        "menu": "list"
    }
    logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - se ha consultado la lista de restaurantes")
    if not lista:
        return render(request, 'restaurantes/list_empty.html', context)
    return render(request, 'restaurantes/list.html', context)

def search(request):
    cocina = request.GET.get('cocina')
    lista = restaurants.objects(cuisine__icontains=cocina)
    context = {
        "resta": lista
    }
    logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - se han consultado los restaurantes con cocina " + cocina)
    return render(request, 'restaurantes/list.html', context)

def restaurant(request, id):
    r = restaurants.objects(restaurant_id=id)[0]
    host = request.get_host()
    context = {
        "resta": r,
        "host": host
    }
    logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - se ha consultado el restaurante con id " + str(r.restaurant_id))
    return render(request, 'restaurantes/restaurant.html', context)

@login_required
def add(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            cuisine = form.cleaned_data['cuisine']
            borough = form.cleaned_data['borough']

            api_base_url = 'http://maps.googleapis.com/maps/api/geocode/xml?address='
            req = api_base_url + name + city

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

            r.name = name
            r.restaurant_id = restaurants.objects.count() + 1
            r.cuisine = cuisine
            r.borough = borough
            r.address = a

            if len(request.FILES) != 0:
                r.photo.put(request.FILES['photo'], content_type = request.FILES['photo'].content_type)

            r.save()
            logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - se ha añadido el restaurante con id " + str(r.restaurant_id))
            return redirect('list')
    else:
        logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - se ha consultado la página para agregar un restaurante")
        form = RestaurantForm();

    context = {
        "form": form,
        "menu": "add"
    }
    return render(request, 'restaurantes/add.html', context)

def show_image(request, id):
    r = restaurants.objects(restaurant_id=id)[0]
    image = r.photo.read()
    logger.info(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " - se ha consultado la imagen del restaurante con id " + str(r.restaurant_id))
    return HttpResponse(image, content_type="image/" + r.photo.format)

def number_of_restaurants(request):
    n = restaurants.objects.count()
    return JsonResponse({'n': n})
