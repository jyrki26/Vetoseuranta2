from application import app, db
from flask import redirect, render_template, request, url_for
from application.teams.models import Team

@app.route("/teams", methods=["GET"])
def teams_index():
    return render_template("teams/list.html", teams = Team.query.order_by(Team.name).all())

@app.route("/teams/new/")
def teams_form():
    return render_template("teams/new_team.html")

@app.route("/teams/<team_id>/", methods=["POST"])
def teams_change_name(team_id):

    t = Team.query.get(team_id)
    t.name = request.form.get("name")
    db.session().commit()
    
    return redirect(url_for("teams_index"))
    
@app.route("/teams/", methods=["POST"])
def teams_create():
    t = Team(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("teams_index"))
