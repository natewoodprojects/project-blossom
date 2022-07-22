from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RegisterForm(FlaskForm):
    email = StringField("Your email: ")
    password = StringField("Your password: ")
    submit = SubmitField("Create User")

class LoginForm(FlaskForm):
    email = StringField("Your email: ")
    password = StringField("Your password: ")
    login = SubmitField("Login")