# Tarea 10

## Despliegue

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

### Contendor db

```
sudo docker build -t restaurantator_db_img db/
sudo docker run -d --name restaurantator_db restaurantator_db_img
```

* Con el archivo `mongodb` se consigue que Mongo pueda escuchar todas las interfaces de red y no solo *localhost*.

### Contenedor app

```
sudo docker build -t restaurantator_app_img app/
sudo docker run -d --name restaurantator_app --link restaurantator_db restaurantator_app_img
```

* El archivo `app.ini` contiene la configuración de uWSGI.
* El archivo `supervisord.conf` tiene la configuración del supervisor (se le indica dónde está `app.ini`).
* Se modofica el archivo `models.py` para aplicar los cambios necesarios para que lea la base de datos de otro contenedor en lugar de en local.
* Se modifica el archivo `settings.py` para aplicar los cambios necesarios para desplegar la app en un contenedor docker en lugar de en local.

### Contenedor nginx

```
sudo docker build -t restaurantator_nginx_img nginx/
sudo docker run -d --name restaurantator_nginx --link restaurantator_app -p 80:80 restaurantator_nginx_img
```

* En el fichero `uwsgi.conf` se encuenta la configuración de nginx.
* En `static/` se encuentran todos los ficheros estáticos para que posteriormente pueda acceder la app a estos.
