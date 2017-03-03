from flask import Flask, Response
app = Flask(__name__)

@app.route('/un_texto_plano')
def texto_plano():
    response = Response()
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    response.set_data("Sirviendo texto plano")
    return response
