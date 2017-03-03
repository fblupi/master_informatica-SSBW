from flask import Flask, Response
app = Flask(__name__)

@app.route('/un_texto_plano')
def texto_plano():
    response = Response()
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    response.set_data("Sirviendo texto plano")
    return response

@app.route('/contenido_html')
def contenido_html():
    return 'Contenido <br>html</br>'

@app.route('/una_imagen')
def imagen():
    f = open('img/deer.jpg', 'rb')
    imagen = f.read()
    response = Response()
    response.headers['Content-Type'] = 'image/jpg'
    response.set_data(imagen)
    return response

@app.route('/este_texto_plano/<lo_que_sea>')
def lo_que_sea(lo_que_sea):
    response = Response()
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    response.set_data(lo_que_sea)
    return response
