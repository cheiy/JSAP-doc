# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class Doctor(UserMixin, db.model):
    """
    Create a Doctors table
    """

    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(55), index = True, unique = True)
    first_name = db.Column(db.String(55), index = True)
    last_name = db.Column(db.String(55), index = True)
    phone_number = db.Column(db.Integer, index = True)
    email = db.Column(db.String(50), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    appointments = db.relationship('Appointment', backref='doctor', lazy='dynamic')

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
    return Doctor.query.get(int(user_id))

class Patient(db.Model):
    """
    Patients table
    """

    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(60), index = True)
    second_name = db.Column(db.String(60), index = True)
    surname = db.Column(db.String(60), index = True)
    gender = db.Column(db.String(6), index = True)
    age = db.Column(db.Integer)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(60), index = True, unique = True)
    appointments = db.relationship('Appointment', backref='patient', lazy='dynamic')

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed value
        """
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        """
        Magic method to return patient username
        """
        return '<Patient: {}>'.format(self.username)


class Appointment(db.Model):
    """
    Create an Appointments table
    """

    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.String(60), unique = True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))

    def __repr__(self):
        """
        Magic method to return appointment date
        """
        return '<Date: {}'.format(self.date)
