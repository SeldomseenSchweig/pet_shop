from email.policy import default
from unicodedata import category, name
from xmlrpc.client import boolean
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, URLField, TextAreaField
from wtforms.validators import InputRequired, Optional, NumberRange, AnyOf

class PetForm(FlaskForm):
    """Adds pet to form"""
    name = StringField("Name: ", validators=[InputRequired("Please input a name")])
    species = StringField("Species (cat, dog, or porcupine) : ", validators=[InputRequired("Please input a species"), AnyOf(values=["porcupine", "dog","cat"])])
    age = IntegerField("Age (between 1-30): ", validators=[Optional(),NumberRange(min=0, max=30, message=" Please put in a number between 0 - 30")])
    photo_url = URLField("Photo -(Optional)",  validators=[Optional()])
    
   
    notes= TextAreaField("Notes (Optional): ")


class EditPetForm(FlaskForm):

    """Form for editing of pets """
    photo_url = URLField("Photo -(Optional)",  validators=[Optional()])
    is_available = BooleanField("Available?")
    notes= TextAreaField("Notes (Optional): ")

