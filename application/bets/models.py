from application import db
from application.models import Base
from application.auth.models import User

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
    bet_type_id = db.Column(
        db.Integer, db.ForeignKey('bet_type.id'), nullable=False)
    bet_result_id = db.Column(
        db.Integer, db.ForeignKey('bet_result.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey(
        'account.id'), nullable=False)


    def __init__(self, date_played, stake, odds, home_team_id, away_team_id, bet_type_id, bet_result_id, account_id):
        self.date_played = date_played
        self.stake = stake
        self.odds = odds
        self.result = 4
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.bet_type_id = bet_type_id
        self.bet_result_id = bet_result_id
        self.account_id = account_id

    def changeResult(self, result):
        self.result = result
    
    @staticmethod
    def find_bet_results(account_id, result):
        stmt = text("SELECT * FROM bet"
                     " LEFT JOIN account ON account.id = bet.account_id "
                     " WHERE (bet.result = :result AND account.id = :account_id)"
                     " ORDER BY bet.date_played").params(account_id = account_id, result=result)
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"date_played":row[3], "home_team_id":row[7], "away_team_id":row[8], "stake":row[4], "odds":row[5], "bet_type":row[9], "bet_result":row[10]})

        return response

    #Shows the bet volumes based on the result
    @staticmethod
    def show_bet_volumes(account_id, result):
        stmt = text("SELECT COUNT(bet.result)"
                     " FROM bet "
                     " LEFT JOIN Account ON account.id = bet.account_id"
                     " WHERE (bet.result = :result AND account.id = :account_id)").params(account_id = account_id, result = result)
        
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"volume":row[0]})

        return response
    
    #Shows the total number of decided bets
    @staticmethod
    def show_bet_count(account_id):
        stmt = text("SELECT COUNT(bet.result)"
                     " FROM bet "
                     " LEFT JOIN Account ON account.id = bet.account_id"
                     " WHERE (bet.result != 4 AND account.id = :account_id)").params(account_id = account_id)
        
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"volume":row[0]})

        return response

    @staticmethod
    def show_bets_per_teams(team_id, account_id, bet_result):
        stmt = text("SELECT COUNT(bet.result)"
                     " FROM bet "
                     " LEFT JOIN Team ON Team.id = Bet.home_team_id OR Team.id = Bet.away_team_id"
                     " LEFT JOIN Account ON account.id = bet.account_id"
                     " WHERE Team.id = :team_id AND Account.id = :account_id AND Bet.result = :bet_result").params(team_id = team_id, account_id = account_id, bet_result = bet_result)
        
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"volume":row[0]})

        return response

    @staticmethod
    def show_bets_per_all(team_id, account_id):
        stmt = text("SELECT COUNT(bet.result)"
                     " FROM bet "
                     " LEFT JOIN Team ON Team.id = Bet.home_team_id OR Team.id = Bet.away_team_id"
                     " LEFT JOIN Account ON account.id = bet.account_id"
                     " WHERE Team.id = :team_id AND Account.id = :account_id AND Bet.result != 4").params(team_id = team_id, account_id = account_id)
        
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"volume":row[0]})

        return response    

Bet_typeBet_results = db.Table('bet_typeBet_result', Base.metadata,
    db.Column('bet_type', db.Integer, db.ForeignKey('bet_type.id')),
    db.Column('bet_result', db.Integer, db.ForeignKey('bet_result.id'))
)

class Bet_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(40), nullable = False)
    bet_results = db.relationship(
                "Bet_result",
                secondary=Bet_typeBet_results,
                backref ="bet_type")

    def __init__(self, type):
        self.type = type
    
    def __str__(self):
        return self.type

class Bet_result(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    result = db.Column(db.String(40), nullable = False)
    bet_types = db.relationship(
                "Bet_type",
                secondary=Bet_typeBet_results,
                backref ="bet_result")

    def __init__(self, result):
        self.result = result

    def __str__(self):
        return self.result

# Initial database insertions

def init_db():
    if db.session.query(Bet_type).count() == 0:
        ah = Bet_type("Aasialainen tasoitusveto")
        eh = Bet_type("Eurooppalainen tasoitusveto")
        
        db.session.add(ah)
        db.session.add(eh)

        h1 = Bet_result("Koti -0,5")
        h2 = Bet_result("Koti +0,5")
        h3 = Bet_result("Koti -1")
        h4 = Bet_result("Koti +1")

        a1 = Bet_result("Vieras -0,5")
        a2 = Bet_result("Vieras +0,5")
        a3 = Bet_result("Vieras -1")
        a4 = Bet_result("Vieras +1")

        d = Bet_result("Tasapeli")

        ah.bet_result.append(h1)
        ah.bet_result.append(h2)
        ah.bet_result.append(h3)
        ah.bet_result.append(h4)

        ah.bet_result.append(a1)
        ah.bet_result.append(a2)
        ah.bet_result.append(a3)
        ah.bet_result.append(a4)

        eh.bet_result.append(h3)
        eh.bet_result.append(h4)
        eh.bet_result.append(a3)
        eh.bet_result.append(a4)
        eh.bet_result.append(d)

        db.session.commit()