# Tarea 1

## Enunciado

### 1.- Sirviendo contenidos

En esta tarea serviremos distintos tipos de contendios al navegador: texto plano, html, imágenes. Para esto hay que cambiar la cabecera de HTTP ['Content-Type'](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type), donde se especifica el [tipo mime](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types) del envio.

La aplicación que hagamos, servirá:

URL | Contenido
-- | --
"/un_texto_plano" | 'Sirviendo texto plano'
"/contenido_html" | 'Contenido **html**'
"/una_imagen" | La imágen, para visualizarla en el navegador
"/este_texto_plano/lo que sea" | 'lo que sea'

Para ello usaremos [Flask](http://flask.pocoo.org/), un 'microframework' de python. En En [Quickstart](http://flask.pocoo.org/docs/0.12/quickstart/), hay una introducción a su uso.

Es conveniente, activar el ambiente de depuración durante la fase de desarrollo: [Configuration Handling](http://flask.pocoo.org/docs/0.12/config/).

Las cabeceras se pueden cambiar con la función [make_response](http://flask.pocoo.org/docs/0.12/quickstart/#about-responses).

### 2.- Sitio web estático con plantillas

Lo normal es usar [plantillas](http://flask.pocoo.org/docs/0.12/tutorial/templates/) para generar el html. Flask usa las plantillas de [Jinja2](http://jinja.pocoo.org/docs/2.9/templates/)

Podemos hacerlo siguiendo el tutorial de [An Introduction to Python’s Flask Framework](https://code.tutsplus.com/tutorials/an-introduction-to-pythons-flask-framework--net-28822).

Y lo podemos completar añadiendo [una página de error](http://flask.pocoo.org/docs/0.12/patterns/errorpages/).

## Instrucciones de uso

```
virtualenv -p python3 venv
source venv/bin/activate
pip install Flask
```
