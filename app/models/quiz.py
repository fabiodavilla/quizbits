from app import db
from datetime import datetime


class Quiz(db.Model):
    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, name, content, user_id):
        self.name = name
        self.content = content
        self.created_at = datetime.now()
        self.user_id = user_id

    def __repr__(self):
        return '<Quiz %r>' % (self)
