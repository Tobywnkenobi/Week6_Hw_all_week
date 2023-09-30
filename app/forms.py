from flask_wtf import FlaskForm
from wtforms import Stringfield, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginDForm(FlaskForm):
    username = SubmitField ('Username or Email')

