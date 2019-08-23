from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.teams.models import Team
from application.teams.forms import TeamForm, ChangeName

@app.route("/teams", methods=["GET"])
@login_required(role="ANY")
def teams_index():
    return render_template("teams/list.html", teams = Team.query.order_by(Team.name).all(), form = ChangeName())

@app.route("/teams/new/")
@login_required(role='1')
def teams_form():
    return render_template("teams/new_team.html", form = TeamForm())

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
