from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.bets.models import Bet, Bet_type, Bet_result
from application.teams.models import Team
from application.bets.forms import BetForm, OpenBetForm, BetSearchForm

@app.route("/bets/", methods=["GET"])
@login_required(role="ANY")
def open_bets():
    return render_template("bets/open_bets.html", bets = Bet.query.filter_by(result=4).order_by(Bet.date_played).all(), teams = Team.query.all(), bet_types = Bet_type.query.all(), bet_results = Bet_result.query.all(), form = OpenBetForm())

@app.route("/bets/new/", methods=["GET"])
@login_required(role="ANY")
def bets_form():
    return render_template("bets/new_bet.html", form = BetForm())

@app.route("/bets/new", methods=["GET", "POST"])
@login_required(role="ANY")
def bets_create():
    form = BetForm(request.form)

    if not form.validate():
        return render_template("bets/new_bet.html", form = form)

    b = Bet(form.date_played.data, form.stake.data, form.odds.data, form.home_team.data.id, form.away_team.data.id, form.bet_type.data.id, form.bet_result.data.id, account_id = current_user.id)

    db.session().add(b)
    db.session().commit()

    return redirect(url_for("open_bets"))

@app.route("/bets/<bet_id>/", methods=["POST"])
@login_required(role="ANY")
def bet_change_status(bet_id):
    form = OpenBetForm(request.form)

    b = Bet.query.get(bet_id)
    
    d = form.results.data
    if d == 'correct':
        b.result = 1
    if d == 'failed':
        b.result = 2
    if d == 'void':
        b.result = 3
    if d == 'delete':
        db.session().delete(b)
    
    db.session().commit()
    
    return redirect(url_for("open_bets"))

@app.route("/bets/search/", methods=["GET"])
@login_required(role="ANY")
def bet_search():
    return render_template("bets/search.html", find_results = Bet.find_bet_results(current_user.id, 1), teams = Team.query.all(), bet_types = Bet_type.query.all(), bet_results = Bet_result.query.all(), form = BetSearchForm())

@app.route("/bets/search/", methods=["POST"])
@login_required(role="ANY")
def bet_search_results():
    form = BetSearchForm(request.form)


    d = form.search.data
    if d == 'correct':
        return render_template("bets/search.html", find_results = Bet.find_bet_results(current_user.id, 1), teams = Team.query.all(), bet_types = Bet_type.query.all(), bet_results = Bet_result.query.all(), form = BetSearchForm())
    if d == 'failed':
        return render_template("bets/search.html", find_results = Bet.find_bet_results(current_user.id, 2), teams = Team.query.all(), bet_types = Bet_type.query.all(), bet_results = Bet_result.query.all(), form = BetSearchForm())
    if d == 'void':
        return render_template("bets/search.html", find_results = Bet.find_bet_results(current_user.id, 3), teams = Team.query.all(), bet_types = Bet_type.query.all(), bet_results = Bet_result.query.all(), form = BetSearchForm())

@app.route("/bets/summary/", methods=["GET"])
@login_required(role="ANY")
def bet_summary():
    return render_template("bets/summary.html", correct = Bet.show_bet_volumes(current_user.id, 1), failed = Bet.show_bet_volumes(current_user.id, 2), void = Bet.show_bet_volumes(current_user.id, 3), addition = Bet.show_bet_count(current_user.id))