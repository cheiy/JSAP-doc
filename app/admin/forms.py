# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, RadioField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Doctor


class AdminLoginForm(FlaskForm):
    """
    Create an admin login form
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Admin Login')

class DoctorsForm(FlaskForm):
    """
    Create a new doctor form
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First_Name', validators=[DataRequired()])
    last_name = StringField('Last_Name', validators=[DataRequired()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    kmpdc_license_num = StringField('KMPDC_License_Num',
                                    validators=[DataRequired()])
    specialization = StringField('Specialization',
                                 validators=[DataRequired()])
    gender = RadioField('Gender', choices=['Male', 'Female'],
                        validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         EqualTo('confirm_password')]
                             )
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')
    
    def validate_email(self, field):
        if Doctor.query.filter_by(email=field.data).first():
            raise ValidationError('Email already in use')

    def validate_kmpdc_license_num(self, field):
        if Doctor.query.filter_by(kmpdc_license_num=field.data).first():
            raise ValidationError('KMPDC License Number already in use')
    
