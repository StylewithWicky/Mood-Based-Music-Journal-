from app import app
from models import db, User, EmotionType, MoodLog
from datetime import datetime

with app.app_context():
    db.drop_all()
    db.create_all()

    # --- Seed Users ---
    users = [
        User(username="john_doe", email="john@example.com"),
        User(username="jane_doe", email="jane@example.com"),
    ]
    db.session.add_all(users)
    db.session.commit()

    # --- Seed Emotion Types ---
    emotions = [
        EmotionType(name="Happy"),
        EmotionType(name="Sad"),
        EmotionType(name="Angry"),
        EmotionType(name="Anxious"),
        EmotionType(name="Grateful"),
    ]
    db.session.add_all(emotions)
    db.session.commit()

    # --- Seed Mood Logs ---
    moods = [
        MoodLog(
            mood="Grateful",
            journal_entry="Had a peaceful walk this morning.",
            user_id=users[0].id,
            emotion_type_id=emotions[4].id,  # Grateful
            created_at=datetime(2025, 6, 27, 8, 0)
        ),
        MoodLog(
            mood="Anxious",
            journal_entry="Too many meetings today.",
            user_id=users[1].id,
            emotion_type_id=emotions[3].id,  # Anxious
            created_at=datetime(2025, 6, 27, 10, 0)
        )
    ]
    db.session.add_all(moods)
    db.session.commit()

    print("✅ Seeded database successfully.")
