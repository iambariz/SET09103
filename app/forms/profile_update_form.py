from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional

class ProfileUpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email address', validators=[DataRequired(), Email()])
    old_password = PasswordField('Current Password', validators=[Optional(), Length(min=6)])
    new_password = PasswordField('New Password', validators=[Optional(), Length(min=6)])
    repeat_password = PasswordField('Repeat New Password', validators=[Optional(), Length(min=6)])
    submit = SubmitField('Save Changes')
