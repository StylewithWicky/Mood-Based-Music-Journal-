from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from . import db


class MoodLog(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    mood=db.Column(db.String , nullable=False)
    journal_entry=db.Column(db.Text)
    created_at=db.Column(db.DateTime ,default=datetime.utcnow)


    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    emotion_type_id = db.Column(db.Integer, db.ForeignKey('emotion_types.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "mood": self.mood,
            "journal_entry": self.journal_entry,
            "created_at": self.created_at.isoformat(),
            "user": self.user.to_dict() if self.user else None,
            "emotion_type": self.emotion_type.to_dict() if self.emotion_type else None
        }