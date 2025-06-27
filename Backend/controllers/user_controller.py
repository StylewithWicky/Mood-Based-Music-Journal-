from flask import Blueprint, request, jsonify
from models import db, User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({'error': 'Username and email are required'}), 400

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])
