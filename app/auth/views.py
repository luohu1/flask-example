from flask import render_template

from . import app


@app.route('/login')
def login():
    return render_template('auth/login.html', content="Login Page.")


@app.route('/logout')
def logout():
    return render_template('auth/logout.html', content="Logout Page.")
