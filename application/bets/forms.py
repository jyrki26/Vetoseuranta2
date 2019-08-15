from flask_wtf import FlaskForm
from wtforms import StringField, DateField, DecimalField, SelectMultipleField, SelectField, validators
from wtforms.widgets import CheckboxInput, ListWidget, TableWidget
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application import db
from application.teams.models import Team


def get_teams():
    return Team.query.order_by(Team.name)


class BetForm(FlaskForm):

    date_played = DateField(
        "Ottelupäivä (dd.mm.yyyy)", [validators.input_required()], format='%d.%m.%Y')
    stake = DecimalField("Panos", [validators.input_required()])
    odds = DecimalField("Kerroin", [validators.input_required()])
    home_team = QuerySelectField(
        "Kotijoukkue", query_factory=get_teams, allow_blank=False)
    away_team = QuerySelectField(
        "Vierasjoukkue", query_factory=get_teams, allow_blank=False)

    class Meta:
        csrf = False


class OpenBetForm(FlaskForm):
    results = SelectField('Tulos', choices=[('correct', 'Oikein'), ('failed', 'Väärin'), ('void', 'Mitätön'), ('delete', 'Poista veto')])
    
    class Meta:
        csrf = False


class BetSearchForm(FlaskForm):
    search = SelectField('Vetojen tulokset', choices=[('correct', 'Oikein'), ('failed', 'Väärin'), ('void', 'Mitätön')])

    class Meta:
        csrf = False