from flask import Blueprint, jsonify,request
from models import EmotionType,db

emotion_bp = Blueprint('emotion_bp', __name__)

@emotion_bp.route('/emotions/<int:id>', methods=['PUT'])
def update_emotion(id):
    emotion = EmotionType.query.get(id)
    if not emotion:
        return jsonify({'error': 'EmotionType not found'}), 404

    data = request.get_json()
    emotion.name = data.get('name', emotion.name)
    db.session.commit()

    return jsonify(emotion.to_dict())

@emotion_bp.route('/emotions/<int:id>', methods=['DELETE'])
def delete_emotion(id):
    emotion = EmotionType.query.get(id)
    if not emotion:
        return jsonify({'error': 'EmotionType not found'}), 404

    db.session.delete(emotion)
    db.session.commit()
    return jsonify({'message': 'EmotionType deleted successfully'})
