from database import db

class User(db.Model):
    # __table_args__ = {"schema": "demo"}
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age
