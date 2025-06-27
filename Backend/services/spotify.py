# services/spotify.py

import requests
import base64
from config import Config

def get_spotify_token():
    client_id = Config.SPOTIFY_CLIENT_ID
    client_secret = Config.SPOTIFY_CLIENT_SECRET
    credentials = f"{client_id}:{client_secret}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    return response.json().get("access_token")
