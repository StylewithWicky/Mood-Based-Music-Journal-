from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from . import db


class MoodLog(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    mood=db.Column(db.String , nullable=False)
    journal_entry=db.Column(db.Text)
    created_at=db.Column(db.DateTime ,default=datetime.utcnow)