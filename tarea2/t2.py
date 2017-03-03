from flask import Flask, session, redirect, url_for, escape, request, render_template
app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def home():
    if 'username' in session:
        return render_template('text.html')
    return render_template('sign-in.html')

@app.route('/imagen')
def imagen():
    if 'username' in session:
        return render_template('image.html')
    return render_template('sign-in.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['inputUsername']
        return redirect(url_for('home'))
    return render_template('sign-in.html')

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('home'))
    return render_template('sign-in.html')

if __name__ == '__main__':
    app.run(debug=True)
