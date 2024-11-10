from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    # username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    repeat = PasswordField('Repeat Password', validators=[DataRequired(), Length(min=6)])
    terms = BooleanField('I accept the terms and conditions', validators=[DataRequired()])
    submit = SubmitField('Register')
