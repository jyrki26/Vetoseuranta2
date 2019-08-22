from application import db
from application.models import Base

from sqlalchemy.sql import text


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

    def changeResult(self, result):
        self.result = result
    
    @staticmethod
    def find_bet_results(account_id, result):
        stmt = text("SELECT * FROM bet"
                     " LEFT JOIN account ON account.id = bet.account_id "
                     " WHERE (bet.result IS :result AND account.id IS :account_id)"
                     " ORDER BY bet.date_played").params(account_id = account_id, result=result)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"date_played":row[3], "home_team_id":row[7], "away_team_id":row[8], "stake":row[4], "odds":row[5]})

        return response
