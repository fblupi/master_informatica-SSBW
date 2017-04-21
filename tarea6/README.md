# Tarea 6

## Autentificación de usuarios y registro (logs)

### Autentificación

En esta tarea completaremos el ['back-end'](https://en.wikipedia.org/wiki/Front_and_back_ends) de nuestra aplicación añadiendo la autentificación de usarios y un sistema de registro (logs).

Django tiene todo lo necesario para el autentificar usuarios, incluyendo tablas, formularios, etc. Pero hay un plugin para Django que facilita todo esto: [django-registration-redux](https://django-registration-redux.readthedocs.io/en/latest/), que incluye también las plantillas, el registro en uno o dos pasos (con activación de la cuenta por e-mail), gestión de la contraseña olividada con tokens, etc.

```
pip install django-regristration-redux
```

Y seguimos los pasos de [User Authentication with Django-Registration-Redux](http://www.tangowithdjango.com/book17/chapters/login_redux.html), incluyendo `'registration'` en las **INSTALLED_APPS** de `settings.py`, y las rutas en `urls.py`.

Como indica el tutorial, las plantillas las podemos coger de [macdhuibh/django-registration-templates](https://github.com/macdhuibh/django-registration-templates) y las modificamos con boostrap, para que queden como [esta](http://getbootstrap.com/examples/signin/) o similar.

Ahora ya podremos gestinar la autorización de usuarios en las vistas, simplemente incluyendo el decorador `@login_required` antes de cada 'vista' de Django: [login required decorator](https://docs.djangoproject.com/en/1.10/topics/auth/default/#the-login-required-decorator).

### Registro

Django tiene un módulo para registro ([Django Logging](https://docs.djangoproject.com/en/1.10/topics/logging/)), basado en el de [python](https://docs.python.org/3.6/library/logging.html).

La configuración del registro, se pone el archivo `settings.py`, y puede ser algo así:

```python
LOG_FILE = 'mi_archivo_de.log'

LOGGING = {
    'version': 1,

    'disable_existing_loggers': False,

    'formatters': {

        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },

        'simple': {
            'format': '%(levelname)s [%(name)s:%(lineno)s] %(message)s'
        },
    },

    'handlers': {

        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, LOG_FILE),
            'formatter': 'verbose',
            'mode':'w'
        },

        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },

    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'ERROR',
        },

        'restaurantes': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
    }
}
```

## Instrucciones de uso

```
virtualenv -p python3 venv
source venv/bin/activate
pip install Django
pip install mongoengine
pip install Pillow
pip install lxml
pip install django-registration-redux
cd sitio_web
python manage.py migrate
python manage.py runserver
```

Ahora solo se podrá añadir un nuevo restaurante si se ha iniciado sesión.
