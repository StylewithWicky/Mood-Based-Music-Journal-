from flask import Blueprint, jsonify
from models import EmotionType

emotion_bp = Blueprint('emotion_bp', __name__)

@emotion_bp.route('/emotions', methods=['GET'])
def get_emotions():
    emotions = EmotionType.query.all()
    return jsonify([e.to_dict() for e in emotions])


