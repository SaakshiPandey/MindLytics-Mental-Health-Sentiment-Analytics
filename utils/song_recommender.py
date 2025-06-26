import json
import random

def load_song_db(path="assets/song_list.json"):
    with open(path, "r") as f:
        return json.load(f)

def get_songs_by_emotion(emotion, count=3):
    db = load_song_db()
    songs = db.get(emotion.lower(), [])
    if len(songs) < count:
        return songs
    return random.sample(songs, count)

