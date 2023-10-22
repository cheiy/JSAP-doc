# app/views.py

from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/landingpage.html', title="Welcome")
@home.route('/registration.html')
def registration():
    """
    Render the registration form for doctors
    """
    return render_template('home/registration.html', title='Are you a doctor? Enter your details here')

@home.route('/appointment.html')
def appointment():
    """
    Render the appointment form for patients
    """
    return render_template('home/appointment.html', title="Schedule an appointment")

@home.route('/login.html')
def login():
    """
    Render the login form
    """
    return render_template('home/login.html', title="Login")

