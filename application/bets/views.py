from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.bets.models import Bet
from application.teams.models import Team
from application.bets.forms import BetForm, OpenBetForm

@app.route("/bets/", methods=["GET"])
@login_required
def open_bets():
    return render_template("bets/open_bets.html", bets = Bet.query.filter_by(result=4).order_by(Bet.date_played).all(), teams = Team.query.all(), form = OpenBetForm())

@app.route("/bets/new/", methods=["GET"])
@login_required
def bets_form():
    return render_template("bets/new_bet.html", form = BetForm())

@app.route("/bets/new", methods=["GET", "POST"])
@login_required
def bets_create():
    form = BetForm(request.form)

    if not form.validate():
        return render_template("bets/new_bet.html", form = form)

    b = Bet(form.date_played.data, form.stake.data, form.odds.data, form.home_team.data.id, form.away_team.data.id, account_id = current_user.id)

    db.session().add(b)
    db.session().commit()

    return redirect(url_for("teams_index"))