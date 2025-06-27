import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'moods.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY='your_secret_key'
    SPOTIFY_CLIENT_ID = "235b3e698a104fa9b40deb55879722f4"
    SPOTIFY_CLIENT_SECRET = "63cf8fb0779443cdab222b396c5c891e"
