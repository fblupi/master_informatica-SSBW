from flask import Flask, Response
app = Flask(__name__)

@app.route('/un_texto_plano')
def texto_plano():
    response = Response()
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    response.set_data("Sirviendo texto plano")
    return response

@app.route('/una_imagen')
def imagen():
    f = open('img/deer.jpg', 'rb')
    imagen = f.read()
    response = Response()
    response.headers['Content-Type'] = 'image/jpg'
    response.set_data(imagen)
    return response
