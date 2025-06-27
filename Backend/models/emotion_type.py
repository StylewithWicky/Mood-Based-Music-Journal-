from . import db

class EmotionType(db.Model):
    __tablename__ = 'emotion_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    mood_logs = db.relationship('MoodLog', backref='emotion_type', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
