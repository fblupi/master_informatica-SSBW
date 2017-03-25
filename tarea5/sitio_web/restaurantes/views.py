from django.shortcuts import render, HttpResponse
from .models import restaurants
from .forms import RestaurantForm

# Create your views here.

def index(request):
    return render(request, 'restaurantes/index.html')

def list(request):
    context = {
        "resta": restaurants.objects[:5], # los cinco primeros
    }
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
            form.save()
            return redirect('list')
    else:
        form = RestaurantForm();

    # GET o error
    context = {
        'form': form,
    }

    return render(request, 'restaurantes/add.html', context)
