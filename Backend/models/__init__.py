from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


from mood import MoodLog
from emotion_type import EmotionType
from user import User
