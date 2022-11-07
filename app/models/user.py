from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    quiz = db.relationship("Quiz")
    answer = db.relationship("Answer")

    def __init__(self, name, email, password, status):
        self.name = name
        self.email = email
        self.password = password
        self.status = status
        self.created_at = datetime.now()

    def __repr__(self):
        return '<User %r>' % (self)
