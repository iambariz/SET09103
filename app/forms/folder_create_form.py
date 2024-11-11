from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FolderCreateForm(FlaskForm):
    name = StringField('Folder name', validators=[DataRequired()])
