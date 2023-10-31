# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from . forms import RegistrationForm, LoginForm
from .. import db
from .. models import Patient


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Handle requests to the signup route
    Add a new patient to the database
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        patient = Patient(email=form.email.data,
                          first_name=form.first_name.data,
                          second_name=form.second_name.data,
                          surname=form.surname.data,
                          gender=form.gender.data,
                          age=form.age.data,
                          password=form.password.data)

        # Add patient to the database
        db.session.add(patient)
        db.session.commit()
        flash('You have registered successfully')

        # Redirect patient to the login page
        return redirect(url_for('auth.login'))

    # load the registration page
    return render_template('auth/registration.html', form=form, title='SignUp')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Patient log in
    """
    form = LoginForm()
    patient = Patient.query.filter_by(email=form.email.data).first()
    if patient is not None and patient.verify_password(form.password.data):
        login_user(patient)

        return redirect(url_for('home.dashboard'))
    else:
        flash("Invalid email or password")
    """
    if form.validate_on_submit():
        patient = Patient.query.filter_by(email=form.email.data).first()
        if patient is not None and patient.verify_password(
                form.password.data):
            login_user(patient)

            return redirect(url_for('home.dashboard'))
        else:
            flash('Invalid email or password')
    """
    return render_template('home/login.html', form=form, title='Login')

@login_required
@auth.route('/myprofile', methods=['GET', 'POST'])
def profile():
    """
    Loads the logged in user_profile
    """
    patient = Patient.query.filter_by(id="1").first()
    
    return render_template('auth/user_profile.html', patient=patient, title='My Details')

@login_required
@auth.route('/logout')
def logout():
    """
    Logout route
    """
    logout_user()
    flash("You have logged out successfully")

    # Return the user to the login page
    return render_template('home/loggedout.html', title="Logged out")
