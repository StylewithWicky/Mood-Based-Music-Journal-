from flask import Blueprint, request, jsonify
from models import db, MoodLog, User, EmotionType

mood_bp = Blueprint('mood_bp', __name__)

@mood_bp.route('/moods', methods=['POST'])
def create_mood():
    data = request.get_json()
    mood = data.get('mood')
    journal_entry = data.get('journal_entry')
    user_id = data.get('user_id')
    emotion_type_id = data.get('emotion_type_id')

    if not all([mood, journal_entry, user_id, emotion_type_id]):
        return jsonify({'error': 'Missing required fields'}), 400

    new_log = MoodLog(
        mood=mood,
        journal_entry=journal_entry,
        user_id=user_id,
        emotion_type_id=emotion_type_id
    )
    db.session.add(new_log)
    db.session.commit()

    return jsonify(new_log.to_dict()), 201


@mood_bp.route('/moods/<int:id>', methods=['PUT'])
def update_mood(id):
    mood = MoodLog.query.get(id)
    if not mood:
        return jsonify({'error': 'MoodLog not found'}), 404

    data = request.get_json()
    mood.mood = data.get('mood', mood.mood)
    mood.journal_entry = data.get('journal_entry', mood.journal_entry)
    mood.user_id = data.get('user_id', mood.user_id)
    mood.emotion_type_id = data.get('emotion_type_id', mood.emotion_type_id)
    db.session.commit()

    return jsonify(mood.to_dict())

@mood_bp.route('/moods/<int:id>', methods=['DELETE'])
def delete_mood(id):
    mood = MoodLog.query.get(id)
    if not mood:
        return jsonify({'error': 'MoodLog not found'}), 404

    db.session.delete(mood)
    db.session.commit()
    return jsonify({'message': 'MoodLog deleted successfully'})
