from django.shortcuts import render, HttpResponse, redirect

from .models import restaurants
from .forms import RestaurantForm

def handle_uploaded_file(n, f):
    with open('static/img/restaurants/' + str(n) + '.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

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
        "resta": r,
        "photo": str(r.restaurant_id)
    }
    return render(request, 'restaurantes/restaurant.html', context)

def add(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            if len(request.FILES) != 0:
                handle_uploaded_file(restaurants.objects.count() + 1, request.FILES['photo'])
            r = form.save()
            return redirect('list')
    else:
        form = RestaurantForm();
    # GET o error
    context = {
        'form': form,
    }
    return render(request, 'restaurantes/add.html', context)
