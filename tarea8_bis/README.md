# Tarea 8 bis

## Autentificación con API

En esta tarea añadiremos al autentificación de usuarios a al API REST, según pone en [Authentication](http://www.django-rest-framework.org/api-guide/authentication/), y siguiendo el código de [How to Implement Token Authentication with Django REST Framework](https://chrisbartos.com/articles/how-to-implement-token-authentication-with-django-rest-framework/), y de [Token-based authentication with Django and React](http://geezhawk.github.io/user-authentication-with-react-and-django-rest-framework).

Usaremos autentificación con token simple, para que también valga para apliaciones móviles nativas, que no se llevan bien con las sesiones. Consiste en añadir a la cabecera un token distinto para cada usuario.

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

Ponemos en **settings.py**:

```python
INSTALLED_APPS = (
  ...,
  'registration',
  'rest_framework',
  'rest_framework.authtoken',
  'rest_framework_mongoengine',
  'restaurantes',
)
```

y:

```python
REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.TokenAuthentication',
  ),
  'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
  )
}
```

Para no tener interferencias montaremos la API de autentificación en otra aplicación:

```
python manage.py startapp tokenauth
```

Ahora procederemos a generar los tokens para cada usuario de la BD, con un script:

```python
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

users = User.objects.all()
for user in users:
  token, created = Token.objects.get_or_create(user=user)
  print user.username, token.key
```

Lógicamente también tendríamos que añadir el código para generar el token cuando se cree un usuario, como está en los enlaces del principio:

```python
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)
```

Y ahora hacemos el código para que se devuelva el token con los datos adecuados:

En **urls.py**:

```python
#urls.py
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
  url(r'^obtain-auth-token/$', csrf_exempt(obtain_auth_token))
]
```

Y ya podremos comprobar que funciona:

```
curl localhost:8000/resta/api/restaurants/
curl -X POST -d "username=user&password=pass" localhost:8000/tokenauth/obtain-auth-token/
curl -H "Authorization: Token asdfq4tegasgq365ew35dfg" localhost:8000/resta/api/restaurants/
```

(No olvidar la barra al final)

## Instrucciones de uso

```
virtualenv -p python3 venv
source venv/bin/activate
pip install Django
pip install mongoengine
pip install Pillow
pip install lxml
pip install django-registration-redux
pip install djangorestframework
pip install django-rest-framework-mongoengine
cd sitio_web
python manage.py migrate
python manage.py startapp tokenauth
python manage.py runserver
```
