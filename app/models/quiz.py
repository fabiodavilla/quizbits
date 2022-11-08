from app import db
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin


class Quiz(db.Model, SerializerMixin):
    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    answer = db.relationship("Answer")

    def __init__(self, name, content, user_id, active):
        self.name = name
        self.content = content
        self.active = active
        self.created_at = datetime.now()
        self.user_id = user_id

    def __repr__(self):
        return '<Quiz %r>' % (self)
