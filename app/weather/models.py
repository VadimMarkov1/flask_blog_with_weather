from app import db


class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(2), unique=True, index=True)
    name = db.Column(db.String(100), unique=True, index=True)
    flag = db.Column(db.String(64), unique=True, index=True)
