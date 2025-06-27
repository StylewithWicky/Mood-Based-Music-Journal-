from flask import Blueprint, request, jsonify
from models import db, MoodLog, User, EmotionType

mood_bp = Blueprint('mood_bp', __name__)

@mood_bp.route('/moods', methods=['POST'])
def create_mood():
    data = request.get_json()
    mood = data.get('mood')
    journal = data.get('journal_entry')
    user_id = data.get('user_id')
    emotion_type_id = data.get('emotion_type_id')

    if not mood or not user_id or not emotion_type_id:
        return jsonify({'error': 'Mood, user_id, and emotion_type_id are required'}), 400

   
    user = User.query.get(user_id)
    emotion = EmotionType.query.get(emotion_type_id)
    if not user or not emotion:
        return jsonify({'error': 'Invalid user_id or emotion_type_id'}), 400

    new_log = MoodLog(mood=mood, journal_entry=journal, user_id=user_id, emotion_type_id=emotion_type_id)
    db.session.add(new_log)
    db.session.commit()

    return jsonify(new_log.to_dict()), 201

@mood_bp.route('/moods', methods=['GET'])
def get_moods():
    moods = MoodLog.query.order_by(MoodLog.created_at.desc()).all()
    return jsonify([m.to_dict() for m in moods])
