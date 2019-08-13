from application import db
from application.models import Base


class Bet(Base):

    date_played = db.Column(db.Date, nullable=False)
    stake = db.Column(db.Numeric(scale=2), nullable=False)
    odds = db.Column(db.Numeric(scale=2), nullable=False)
    result = db.Column(db.Integer, nullable=True)
    home_team_id = db.Column(
        db.Integer, db.ForeignKey('team.id'), nullable=False)
    away_team_id = db.Column(
        db.Integer, db.ForeignKey('team.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey(
        'account.id'), nullable=False)


    def __init__(self, date_played, stake, odds, home_team_id, away_team_id, account_id):
        self.date_played = date_played
        self.stake = stake
        self.odds = odds
        self.result = 4
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.account_id = account_id
