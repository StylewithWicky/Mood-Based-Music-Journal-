
from flask import Blueprint, request, jsonify
import requests
from services.spotify import get_spotify_token

music_bp = Blueprint('music_bp', __name__)

MOOD_GENRE_MAP = {
    "Happy": "pop",
    "Sad": "acoustic",
    "Angry": "metal",
    "Anxious": "chill",
    "Grateful": "indie"
}

@music_bp.route('/recommendation', methods=['GET'])
def recommend_song():
    mood = request.args.get("mood")
    genre = MOOD_GENRE_MAP.get(mood, "pop")

    token = get_spotify_token()
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "q": f"genre:{genre}",
        "type": "track",
        "limit": 1
    }

    res = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
    data = res.json()
    if "tracks" in data and data["tracks"]["items"]:
        track = data["tracks"]["items"][0]
        return jsonify({
            "song": track["name"],
            "artist": track["artists"][0]["name"],
            "preview_url": track["preview_url"],
            "url": track["external_urls"]["spotify"]
        })

    return jsonify({"error": "No track found"}), 404
