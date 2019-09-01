from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.teams.models import Team
from application.bets.models import Bet
from application.teams.forms import TeamForm, ChangeName, DeleteTeam
from wtforms.validators import ValidationError

@app.route("/teams", methods=["GET"])
@login_required(role="ANY")
def teams_index():
    return render_template("teams/list.html", teams = Team.query.order_by(Team.name).all(), form = ChangeName())

@app.route("/teams/new/")
@login_required(role='1')
def teams_form():
    return render_template("teams/new_team.html", form = TeamForm())

@app.route("/teams/delete/", methods=["GET"])
@login_required(role="1")
def teams_delete():
    return render_template("teams/delete.html", teams = Team.query.order_by(Team.name).all(), form = DeleteTeam())

@app.route("/teams/delete/<team_id>/", methods=["POST"])
@login_required(role='1')
def delete_team(team_id):
    form = DeleteTeam(request.form)

    if not form.validate():
        return render_template("teams/delete.html", teams = Team.query.order_by(Team.name).all(), form = form)

    t = Team.query.get(team_id)
    d = form.delete.data
    
    if d == 'delete':
        name = bool(Bet.query.filter_by(home_team_id = t.id).first())
        name2 = bool(Bet.query.filter_by(away_team_id = t.id).first())
        if name == True or name2 == True:
            return render_template("teams/delete.html", teams = Team.query.order_by(Team.name).all(), form = form,
                                            error = "Joukkuetta on jo käytetty vedossa, joten sitä ei voi poistaa")
        
        db.session().delete(t)

    db.session().commit()
    
    return redirect(url_for("teams_delete"))

@app.route("/teams/<team_id>/", methods=["POST"])
@login_required(role='1')
def teams_change_name(team_id):
    form = ChangeName(request.form)

    if not form.validate():
        return render_template("teams/list.html", teams = Team.query.order_by(Team.name).all(), form = form)

    t = Team.query.get(team_id)
    t.name = form.name.data

    db.session().commit()
    
    return redirect(url_for("teams_index"))
    
@app.route("/teams/", methods=["POST"])
@login_required(role="ANY")
def teams_create():
    form = TeamForm(request.form)

    if not form.validate():
        return render_template("teams/new_team.html", form = form)

    t = Team(form.name.data)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("teams_index"))
