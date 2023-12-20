from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField


class AddForm(FlaskForm):
    name = StringField("Name of Owner: ")
    id = IntegerField("ID Number of Puppy associated to Owner")
    submit = SubmitField("Add Owner")
