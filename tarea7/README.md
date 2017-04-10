# Tarea 6

## jQuery y AJAX

En esta tarea mejoraremos el [front-end](https://en.wikipedia.org/wiki/Front_and_back_ends) de nuestra aplicación incorporando código con jQuery y llamadas AJAX.

### Resaltado de opción de menú

Pasaar una nueva variable a los templates que sirva para resaltar la opción de menú. Esto se puede hacer [cambiando una propiedad css](http://api.jquery.com/css/), o [cambiando clases](http://fellowtuts.com/jquery/change-class-using-jquery/) usando jQuery.

### AJAX

Añadir una [ventana modal](https://v4-alpha.getbootstrap.com/components/modal/) para mostrar la dirección completa del restaurante haciendo una llamada [AJAX](https://learn.jquery.com/ajax/jquery-ajax-methods/) para conseguir los datos, incluso poniendo una foto de streetview: https://maps.googleapis.com/maps/api/streetview?size=600x300&location=37.1765359,-3.596629699999999
   
## Instrucciones de uso

```
virtualenv -p python3 venv
source venv/bin/activate
pip install Django
pip install mongoengine
pip install Pillow
pip install lxml
pip install django-regristration-redux
cd sitio_web
python manage.py migrate
python manage.py runserver
```
