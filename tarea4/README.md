# Tarea 4

## Enunciado

### Instalación de Django

Para esta tarea instalaremos el framework [Django](https://www.djangoproject.com/), y pasaremos el código y los templatess de las tareas anteriores para que funcionen en Django.

Seguiremos los pasos de [este tutorial](http://drksephy.github.io/2015/07/16/django/):

```
pip install django
django-admin startproject sitio_web
```

que nos creará la estructura de directorios y archivos para nuestras aplicaciones.

Podemos comprobar que funciona iniciando el servidor de desarrollo:

```
cd sitio_web
python manage.py runserver
```

Creamos ahora una aplicación dentro del projecto:

```
python manage.py startapp restaurantes
```

Creamos un directorio para los templates y para los archivos estáticos:

```
mkdir templates
mkdir static
```

y los apuntamos en el archivo `sitio_web/settings.py`:

```python
TEMPLATES = [
{
'DIRS':[os.path.join(BASE_DIR, 'templates')]
...

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

y apuntamos también nuesta aplicación:

```python
INSTALLED_APPS = (
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'restaurantes',
)
```

Ahora podemos iniciar la bases de datos SQL que usaremos para los datos autentificación y registro de usuarios, para los restaurantes seguimos usando mongoDB:

```
python manage.py migrate
```

Esto habrá que hacerlo cada vez que hagamos cambios en la BD SQL.

Creamos ahora un administrador de la BD:

```
python manage.py createsuperuser
```

y tendremos acceso a la aplicación de administración de la BD en: http://localhost:8000/admin

8000 es el puerto por defecto, se puede lanzar desde otro puerto:

```
python manage.py runserver 0.0.0.0:5000
```

Y podemos ahora hacer una aplicación siguiendo los pasos desde el *Step 3: Your first view* del tutorial, pero usando la base de datos de mongo, y las templates de las tareas anteriores.

Solo tendremos que cambiar, el enrutador (ahora en dos archivos aparte):

```python
# sitio_web/urls.py

   from django.conf.urls import include, url
   from django.contrib import admin

   urlpatterns = [
     url(r'^restaurantes/', include('restaurantes.urls')),
     url(r'^admin/', include(admin.site.urls)),
   ]
```

y en un nuevo archivo donde especificamos las rutas que comiencen por `restaurantes/`:

```python
# restaurantes/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test/$', views.test, name='test'),
]
```

El código lo pondremos en el archivo `views.py`:

```python
# views.py

from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    context = {}   # Aquí van la las variables para la plantilla
    return render(request,'test.html', context)
```

Django utiliza una [librería de templates](https://tutorial.djangogirls.org/en/django_templates/), muy parecida al Jinja2 de flask, solo cambian las instrucciones para cargar los archivos estaticos y los nombres de los enlaces:

```jinja2
{% load static %}
...
<link  href="{% static 'css/style.css' %}" rel="stylesheet" media="screen">
...
<a href="{% url 'name para la url' %}"> </a>
```

y en `restaurantes/models.py`, incluimos el esquema de mongoengine, como en *Listing 17* de [Using MongoDB with Django](https://www.ibm.com/developerworks/library/os-django-mongo/):

Algo como:

```python
# views.py
# ----------

from django.shortcuts import render
from .models import restaurants

def listar(requests):
  context = {
    "resta": restaurants.objects[:5], # los cinco primeros
  }
  return render (requests, 'restaurantes/listar.html', context)
```

Poner a funcionar una pantalla de entrada de datos y otra de consulta.

En [django-marcador](http://django-marcador.keimlink.de/) hay un tutorial completo (ojo, usa python 2.7 y django 1.8).
