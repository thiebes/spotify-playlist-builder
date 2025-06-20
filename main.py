import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# === Load credentials from .env ===
load_dotenv()
sp = Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri=os.getenv("REDIRECT_URI"),
    scope="playlist-modify-public"
))

# === Customize these ===
playlist_name = "Test Playlist"
playlist_description = "Created using my general-purpose playlist builder script."

track_list = [
    ("Alright", "Kendrick Lamar"),
    ("Freedom", "Beyoncé"),
    ("Someday We’ll All Be Free", "Donny Hathaway")
]

# === Create the playlist ===
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=True,
    description=playlist_description
)
print(f"\n✅ Created playlist: {playlist['external_urls']['spotify']}\n")

# === Search and add tracks ===
def search_track(title, artist):
    query = f"track:{title} artist:{artist}"
    result = sp.search(q=query, type="track", limit=1)
    items = result.get("tracks", {}).get("items", [])
    return items[0]["uri"] if items else None

for title, artist in track_list:
    uri = search_track(title, artist)
    if uri:
        sp.playlist_add_items(playlist["id"], [uri])
        print(f"✓ Added: {title} – {artist}")
    else:
        print(f"✗ Not found: {title} – {artist}")
