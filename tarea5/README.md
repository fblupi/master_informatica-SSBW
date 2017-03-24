# Tarea 5

## Entrada de datos con formularios

En esta tarea usaremos la clase [Forms](https://docs.djangoproject.com/en/1.10/topics/forms/) de Django para añadir datos. Incluiremos también una foto del restaurante aprovechando el tipo de campo [ImageField](http://docs.mongoengine.org/apireference.html#mongoengine.fields.ImageField), de mongoengine. (Para usarlo hay que instalar la librería [pillow](https://python-pillow.org/))

También haremos una página de detalle con los datos de cada restaurante, incluyendo la foto, a la que se acceda:

```
http://localhost:8000/restaurante/nombre_del_restaurante
```

ó mejor:

```
http://localhost:8000/restaurante/restaurante_id  (que debe ser único)
```

Django [URL dispatcher](https://docs.djangoproject.com/en/1.10/topics/http/urls/#named-groups)

### Pasos

1. Hacer un form compatble con la clase de mongoengine, que incluya algún validador y subir una imagen

2. A la vuelta del form, tener en cuenta la [subida de archivos](https://docs.djangoproject.com/en/1.10/topics/http/file-uploads/) en el formulario ([Binding uploaded files to a form](https://docs.djangoproject.com/en/1.10/ref/forms/api/#binding-uploaded-files)), y que haya un campo de clave única en la BD (puede ser restaurant_id o el nombre). Para guardar la imágen en mongo, simplemente:

```python
restaruante = restaurants(
   name = form.cleaned_data.get('name')  # después de validar
   ...
   foto = request.FILES.get('foto')
)
```

3. Hacer una salida con los datos cada restaurante. Para leer la imágen de la BD: [GridFs](http://docs.mongoengine.org/guide/gridfs.html#gridfs)

Para que quede mejor, se puede utilizar [django-boostrap4](https://github.com/GabrielUlici/django-bootstrap4) o similar

## Instrucciones de uso

```
virtualenv -p python3 venv
source venv/bin/activate
pip install Django
pip install mongoengine
pip install Pillow
pip install lxml
cd sitio_web
python manage.py migrate
python manage.py runserver
```
