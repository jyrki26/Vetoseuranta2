from flask_wtf import FlaskForm
from wtforms import StringField, validators

class TeamForm(FlaskForm):
    name = StringField("Joukkueen nimi", [validators.Length(min=2)])
 
    class Meta:
        csrf = False

class ChangeName(FlaskForm):
    name = StringField("Uusi nimi", [validators.Length(min=2)])

    class Meta:
        csrf = False