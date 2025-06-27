from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models
from .user import User
from .mood import MoodLog
from .emotion_type import EmotionType

