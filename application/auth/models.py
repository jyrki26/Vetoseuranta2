from application import db
from application.models import Base


class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey(
        'role.id'), nullable=False)

    bets = db.relationship("Bet", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def roles(self):
        return str(self.role_id)

# User roles

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)

    def __init__(self, name):
        self.name = name

# Initial database insertions

def init_db():
    if db.session.query(Role).count() == 0:
        admin = Role("ADMIN")
        user = Role("USER")
        
        db.session.add(admin)
        db.session.add(user)
        db.session.commit()