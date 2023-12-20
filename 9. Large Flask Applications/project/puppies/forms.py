from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField


class AddForm(FlaskForm):
    name = StringField("Name of Puppy: ")
    submit = SubmitField("Add Puppy")


class DelForm(FlaskForm):
    id = IntegerField("ID Number of Puppy to remove")
    submit = SubmitField("Remove Puppy")
