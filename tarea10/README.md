# Tarea 10

## Single-page Applications

La última práctica consiste en tener una aplicación web desplegada en un ambiente de 'producción', es decir funcionando con la depuración en 'OFF' y conectada a un servidor web como [nginx](https://www.nginx.com/) o [apache](http://httpd.apache.org/) en el puerto 80.

El despliegue de una aplicación con django, está contada en: [How to deploy with WSGI](https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/), [How to use Django with Gunicorn](https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/gunicorn/), [Deploying Gunicorn](http://docs.gunicorn.org/en/latest/deploy.html), [Supervisor](http://docs.gunicorn.org/en/latest/deploy.html#supervisor), y en las transparencias de clase.

Básicamente consiste en poner la configuración de producción, es decir en el archivo settings.py estarán las variables:

```python
DEBUG = False

ALLOWED_HOSTS = ['*']
```

Con esto dejará de funcionar el servidor de desarrollo, y de servir los contenidos de **/static**, que tendrán que pasar a servirse desde el servidor web de producción. Django tiene un script: [collectstatic](https://docs.djangoproject.com/en/1.10/ref/contrib/staticfiles/) para facilitar pasar los contenidos a otro directorio.

Después habrá que poner funcionar la aplicación con un servidor web [wsgi](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface), (p.e. [gunicorn](http://gunicorn.org/)) y conectar la aplicación, y el resto de servicios que pudiera haber (los arhivos static), a un servidor web que también funcione como [proxy inverso](https://en.wikipedia.org/wiki/Reverse_proxy) (p.e. [nginx](https://www.nginx.com/)) en el puerto 80.

Para automatizar el proceso, podremos hacer algún script con [Makefile](https://en.wikipedia.org/wiki/Makefile),

El despliegue se puede hacer en un contenedor usando [docker](https://www.docker.com/), y [docker-compose](https://docs.docker.com/compose/) (ejemplo con [django](https://docs.docker.com/compose/django/))

## Instrucciones de uso
