import os
from flask import request, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, TextField, MultipleFileField
from wtforms.validators import DataRequired, Length
from werkzeug.utils import secure_filename

# Defines fields for new entry form
class SubmissionForm(FlaskForm):
    musicbrainz_album_id = StringField('MusicBrainz ID', validators=[DataRequired(), Length(min=36, max=36)])
    source = TextField('Source', validators=[DataRequired(), Length(min=5)])
    upload = MultipleFileField('Upload', validators=[FileRequired()])
    submit = SubmitField('Submit')



