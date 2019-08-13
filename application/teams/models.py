from application import db
from application.models import Base

class Team(Base):
    name = db.Column(db.String(144), nullable=False)
    home_team = db.relationship("Bet", foreign_keys='Bet.home_team_id')
    away_team = db.relationship("Bet", foreign_keys='Bet.away_team_id')

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name