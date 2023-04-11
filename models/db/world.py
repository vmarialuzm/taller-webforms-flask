from app import db

class City(db.Model):
    ID=db.Column(db.Integer,autoincrement=True,primary_key=True)
    Name=db.Column(db.String(25))
    CountryCode=db.Column(db.String(3))
    District=db.Column(db.String(20))
    Population=db.Column(db.Integer)