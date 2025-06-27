from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from controllers.mood_controller import mood_bp
from controllers.emotional_controller import emotion_bp
from controllers.user_controller import user_bp
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

# ✅ MOST IMPORTANT LINE — use this!
CORS(app, supports_credentials=True, origins=["http://localhost:5173"])

jwt = JWTManager(app)
db.init_app(app)

with app.app_context():
    db.create_all()

# ✅ Register blueprints
app.register_blueprint(mood_bp)
app.register_blueprint(user_bp)
app.register_blueprint(emotion_bp)

# ✅ auth_bp MUST be registered AFTER CORS is configured
from controllers.auth_controller import auth_bp
app.register_blueprint(auth_bp, url_prefix="/auth")

from controllers.music_controller import music_bp
app.register_blueprint(music_bp)


if __name__ == '__main__':
    app.run(debug=True)
