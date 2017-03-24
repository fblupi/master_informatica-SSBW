from django.shortcuts import render, HttpResponse
from .models import restaurants

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    valor = 3
    context = {
        'variable': valor,
    }   # Aquí van las variables para la plantilla
    return render(request, 'test.html', context)

def listar(request):
    context = {
        "resta": restaurants.objects[:5], # los cinco primeros
    }
    return render(request, 'restaurantes/listar.html', context)

def buscar(request):
    cocina = request.GET.get('cocina')
    lista = restaurants.objects(cuisine__icontains=cocina)
    print (cocina)
    print (lista)
    context = {
        "resta": lista
    }
    return render(request, 'restaurantes/listar.html', context)
