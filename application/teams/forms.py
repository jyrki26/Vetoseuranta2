from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField
from wtforms.validators import ValidationError
from application.teams.models import Team

def check_name(form, field):
     name = bool(Team.query.filter_by(name=field.data).first())
     if name == True:
         raise ValidationError('Samanniminen joukkue on jo tallennettu')

class TeamForm(FlaskForm):
    name = StringField("Joukkueen nimi", [validators.Length(min=2, message= 'Nimen tulee olla vähintään kahden merkin mittainen'), check_name])

    class Meta:
        csrf = False

class ChangeName(FlaskForm):
    name = StringField("Uusi nimi", [validators.Length(min=2, message= 'Nimen tulee olla vähintään kahden merkin mittainen'), check_name])

    class Meta:
        csrf = False

class DeleteTeam(FlaskForm):
    delete = SelectField("Poista joukkue", choices=[("-", "---"), ("delete", "Poista joukkue")])

    def validate_delete(form, field):
        if field.data == '-':
            raise ValidationError('Hyväksy joukkueen poistaminen valitsemalla Poista joukkue')

    class Meta:
        csrf = False