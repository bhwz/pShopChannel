from flask_wtf import FlaskForm
from wtforms import validators, PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField


class RegisterForm(FlaskForm):
    email = EmailField('Email', [validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(message='A password is required.'),
        validators.EqualTo('password_confirm', message='Both passwords must match.'),
        validators.Length(message='Your password must be at least 8 characters.', min=8)
    ])
    password_confirm = PasswordField('Confirm your password')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = EmailField('Email', [validators.Email()])
    password = PasswordField('Password', validators=[validators.DataRequired(message='Your password is needed.')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')
