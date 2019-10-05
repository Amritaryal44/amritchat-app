from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('username_label', validators=[InputRequired(message="Username Required"), Length(min=4, max=25, message="At least size 4 and at most size 25")])
    password = PasswordField('password_label', validators=[InputRequired(message="Password Required"), Length(min=4, max=25, message="At least size 4 and at most size 25")])
    confirm_pswd = PasswordField('confirm_pswd_label', validators=[InputRequired(message="Password Required"), EqualTo('password', message="Password must match")])
    submit_button = SubmitField('Create')