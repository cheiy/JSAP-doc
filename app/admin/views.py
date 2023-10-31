# app/admin/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import admin
from . forms import DoctorsForm, AdminLoginForm
from .. import db
from .. models import Doctor, User


@admin.route('/admin', methods=['GET', 'POST'])
def admin_login():
    """
    Backend for admins to log in
    """
    form = AdminLoginForm()
    user = User.query.filter_by(email=form.username.data).first()
    if user is not None and user.verify_password(form.password.data):
        login_user(user)
        return redirect(url_for('admin.dashboard'))
    else:
        flash("Invalid username or password")
    return render_template('admin/admin_login.html', form=form, title='Login')


@admin.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    """
    Backend for doctors management
    """
    form = DoctorsForm()
    """
    doctor = Doctor(email=form.email.data,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data,
                        phone_number=form.phone_number.data,
                        kmpdc_license_num=form.kmpdc_license_num.data,
                        specialization=form.specialization.data,
                        gender=form.gender.data,
                        password_hash=form.password.data
                        )
        # Add doctor to the database
    db.session.add(doctor)
    db.session.commit()
    flash('Doctor added successfully')
    """
    if form.validate_on_submit():
        doctor = Doctor(email=form.email.data,
                        first_name=form.first_name.data,
                        last_name=form.second_name.data,
                        phone_number=form.phone_number.data,
                        kmpdc_license_num=form.kmpdc_license_num.data,
                        specialization=form.specialization.data,
                        gender=form.gender.data,
                        password_hash=form.password.data
                        )
        # Add doctor to the database
        db.session.add(doctor)
        db.session.commit()
        flash('Doctor added successfully')
    else:
        flash("Unable to add doctor")
    return render_template('admin/add_doctor.html', form=form, title='Add Doctors')

@admin.route('/admin_dashboard', methods=['GET', 'POST'])
def dashboard():
    """
    Admin's Dashboard
    """

    return render_template('admin/admin_dashboard.html', title="Admin Dashboard")