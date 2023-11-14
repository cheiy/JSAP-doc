# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager
from datetime import datetime


class Doctor(UserMixin, db.Model):
    """
    Create a Doctors table
    """

    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(55), index=True)
    last_name = db.Column(db.String(55), index=True)
    phone_number = db.Column(db.Integer, index=True)
    specialization = db.Column(db.String(200), index=True)
    kmpdc_license_num = db.Column(db.String(100), index=True)
    email = db.Column(db.String(50), index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.String(6), index=True, nullable=False)
    appointments = db.relationship('Appointment', backref='doctor',
                                   lazy='dynamic')

    @property
    def password(self):
        """
        Protect password from being accessed
        """
        raise AttributeError('Password is not readable')

    @password.setter
    def password(self, password):
        """
        Set password hash
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if password has matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Doctor: {}>'.format(self.username)


# User loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    """
    Users table
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), index=True)
    second_name = db.Column(db.String(60), index=True)
    surname = db.Column(db.String(60), index=True)
    gender = db.Column(db.String(6), index=True)
    age = db.Column(db.Integer)
    password = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(60), index=True, unique=True, nullable=False)
    appointments = db.relationship('Appointment', backref='patient',
                                   lazy='dynamic')
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, first_name, second_name, surname, gender, age,
                 password, email, is_admin=False, is_confirmed=False,
                 confirmed_on=None):
        self.first_name = first_name
        self.second_name = second_name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.password = generate_password_hash(password)
        self.created_at = datetime.now()
        self.email = email
        self.is_admin = is_admin
        self.is_confirmed = is_confirmed
        self.confirmed_on = confirmed_on

    '''@property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password = generate_password_hash(password)
    '''
    
    def verify_password(self, password):
        """
        Check if password has matches actual password
        """
        return check_password_hash(self.password, password)

    def __repr__(self):
        """
        Magic method to return patient username
        """
        return '<Patient: {}>'.format(self.email)


class Appointment(db.Model):
    """
    Create an Appointments table
    """

    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(60), unique=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))

    def __repr__(self):
        """
        Magic method to return appointment date
        """
        return '<Date: {}'.format(self.date)
