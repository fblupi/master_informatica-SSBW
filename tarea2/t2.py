from flask import Flask, Response, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('text.html')

@app.route('/imagen')
def imagen():
    return render_template('image.html')

if __name__ == '__main__':
    app.run(debug=True)
