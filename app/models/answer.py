from app import db
from datetime import datetime


class Answer(db.Model):
    __tablename__ = 'answer'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    quiz_id = db.Column(db.Integer, db.ForeignKey("quiz.id"))

    def __init__(self, content, user_id, quiz_id):
        self.content = content
        self.user_id = user_id
        self.quiz_id = quiz_id
        self.created_at = datetime.now()

    def __repr__(self):
            return '<Answer %r>' % (self)