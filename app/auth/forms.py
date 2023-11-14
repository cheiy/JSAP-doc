# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, RadioField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import User


class RegistrationForm(FlaskForm):
    """
    Create a new account form
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First_Name', validators=[DataRequired()])
    second_name = StringField('Second_Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    gender = RadioField('Gender', choices=['Male', 'Female'],
                        validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         EqualTo('confirm_password')]
                             )
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
    """
    Patient Log in form
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
