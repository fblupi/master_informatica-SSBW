from django.shortcuts import render, HttpResponse, redirect

from .models import restaurants
from .forms import RestaurantForm

# Create your views here.

def index(request):
    return render(request, 'restaurantes/index.html')

def list(request):
    lista = restaurants.objects
    context = {
        "resta": lista
    }
    if not lista:
        return render(request, 'restaurantes/list_empty.html', context)
    return render(request, 'restaurantes/list.html', context)

def search(request):
    cocina = request.GET.get('cocina')
    lista = restaurants.objects(cuisine__icontains=cocina)
    context = {
        "resta": lista
    }
    return render(request, 'restaurantes/list.html', context)

def restaurant(request, id):
    r = restaurants.objects(restaurant_id=id)[0]
    context = {
        "resta": r
    }
    return render(request, 'restaurantes/restaurant.html', context)

def add(request):
    if request.method == "POST":
        form = RestaurantForm(data=request.POST)
        if form.is_valid():
            r = form.save()
            return redirect('list')
    else:
        form = RestaurantForm();

    # GET o error
    context = {
        'form': form,
    }

    return render(request, 'restaurantes/add.html', context)
