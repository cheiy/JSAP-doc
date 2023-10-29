# app/views.py

from flask import render_template
from flask_login import login_required

from . import home
from ..auth.forms import LoginForm

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/login')
def login():
    """
    Render the login template
    """
    form = LoginForm()
    return render_template('home/login.html', title="Login or Create An Account", form=form)

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the user dashboard
    """
    return render_template('home/dashboard.html', title="Welcome to your homepage")
