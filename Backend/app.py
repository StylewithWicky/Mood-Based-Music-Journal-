from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from controllers.mood_controller import mood_bp
from controllers.emotional_controller import emotion_bp
from controllers.user_controller import user_bp

app=Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(mood_bp)
app.register_blueprint(user_bp)
app.register_blueprint(emotion_bp)

if __name__ == '__main__':
    app.run(debug=True)