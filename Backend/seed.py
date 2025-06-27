from app import app
from models import db, User, EmotionType, MoodLog
from datetime import datetime

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(username="itsjustmaitai", email="itsjustmaitai@gmail.com")
    user1.set_password("pass123")

    user2 = User(username="jane_doe", email="jane@example.com")
    user2.set_password("securepass")
            
    db.session.add_all([user1, user2])
    db.session.commit()
    
    emotions = [
        EmotionType(name="Happy"),
        EmotionType(name="Sad"),
        EmotionType(name="Angry"),
        EmotionType(name="Anxious"),
        EmotionType(name="Grateful"),
    ]
    db.session.add_all(emotions)
    db.session.commit()

   
    moods = [
        MoodLog(
            mood="Grateful",
            journal_entry="Had a peaceful walk this morning.",
            user_id=users[0].id,
            emotion_type_id=emotions[4].id, 
            created_at=datetime(2025, 6, 27, 8, 0)
        ),
        MoodLog(
            mood="Anxious",
            journal_entry="Too many meetings today.",
            user_id=users[1].id,
            emotion_type_id=emotions[3].id,  
            created_at=datetime(2025, 6, 27, 10, 0)
        )
    ]
    db.session.add_all(moods)
    db.session.commit()

    print("✅ Seeded database successfully.")
