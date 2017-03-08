# Tarea 3

## Enunciado

### Persistencia No-SQL

En esta tarea usaremos un Oject Document Mapper para usar la BD [MongoDB](https://docs.mongodb.com/getting-started/shell/introduction/). Así se consigue indepedizar (en parte) el código de la BD. Mongoengine es parecido al [orm de django](https://docs.djangoproject.com/en/1.10/topics/db/models/).

Tendremos que [instalar la BD](https://docs.mongodb.com/getting-started/shell/installation/), y también [mongoengine](http://mongoengine.org/), para acceder a la BD desde python.

### Definir un esquema para la BD, y hacer un script para rellenar la BD

Usaremos la BD [datos de test](https://docs.mongodb.com/getting-started/shell/import-data/) de mongoDB, y haremos un script de poblaciṕon de la BD para añadir algunos restaurantes en Granada, y probar el ODM.

**populate.py**

```python
from mongoengine import *
import datetime

db = connect('test')

# Esquema para la BD de pruebas de mongoDB

class addr(EmbeddedDocument):
    building = StringField()
    street   = StringField()
    city     = StringField()   # añadido
    zipcode  = IntField()
    coord    = GeoPointField() # OJO, al BD de test estan a revés
                               # [long, lat] en vez de [lat, long]

class likes(EmbeddedDocument):
    grade = StringField(max_length=1)
    score = IntField()
    date  = DateTimeField()

class restaurants(Document):
    name             = StringField(required=True, max_length=80)
    restaurant_id    = IntField()
    cuisine          = StringField()
    borough          = StringField()
    address          = EmbeddedDocumentField(addr)              # en la misma collección
    grades           = ListField(EmbeddedDocumentField(likes))


dir = addr(street="Hermosa, 5 ", city="Granada", zipcode=18010, coord=[37.1766872, -3.5965171])  # así están bien
r = restaurants(name="Casa Julio", cuisine="Granaina", borough="Centro", address=dir)
r.save()

# Poner alguno más
# ...

# Consulta, los tres primeros
for r in restaurants.objects[:3]:
    print (r.name, r.address.coord, r.grades[0].date)

# Hacer más consultas, probar las de geolocalización
# ...
```

Se pueden añadir más validaciones, o valores por defecto ([Defining Documents](http://docs.mongoengine.org/guide/defining-documents.html)).

Añadir varios restaurantes y probar las [consultas a la BD](http://docs.mongoengine.org/guide/querying.html). Para averiguar las coordenadas se puede usar el [servicio de geocodificación de google](https://developers.google.com/maps/documentation/geocoding/intro), p.e.: `http://maps.googleapis.com/maps/api/geocode/json?address=Bar+Casa+Julio+Granada`, que devueleve un string [JSON](http://maps.googleapis.com/maps/api/geocode/json?address=Bar+Casa+Juilo+Granada). Para el requerimento se puede usar la librería [requests](http://docs.python-requests.org/en/master/).

## Instrucciones de uso

```
virtualenv -p python3 venv
source venv/bin/activate
pip install Flask
pip install mongoengine
export FLASK_APP=t3.py
flask run
```
