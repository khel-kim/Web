from flask import Flask, render_template
from flask import request, session
import os
app = Flask(__name__)


@app.route('/')
def home():
    print('SESSION:', session)
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"


@app.route('/login/', methods=['POST'])
def do_admin_login():
    print("SESSION:", session)
    print("REQUEST:", request)
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return home()
    else:
        return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
