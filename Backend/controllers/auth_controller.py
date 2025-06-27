from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST', 'OPTIONS'])
@cross_origin(origin='http://localhost:5173', supports_credentials=True) 
def login():
    if request.method == 'OPTIONS':
        return '', 200 

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    print("Received:", email, password)

    
    if email == 'test@example.com' and password == 'secret':
        return jsonify(token="fake-jwt-token"), 200
    return jsonify(error="Invalid credentials"), 401
