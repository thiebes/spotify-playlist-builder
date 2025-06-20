# Spotify Playlist Builder

This is a general-purpose Python script that creates and populates Spotify playlists using the Spotify Web API. You can define a list of songs by title and artist, and the script will search for them, create a new playlist in your account, and add the matched tracks.

Originally built to curate a thematic Juneteenth playlist, the tool is designed to be flexible for any use case involving playlist automation or structured listening guides.

## Features

* Authenticate securely with Spotify using OAuth2
* Create new playlists with custom names and descriptions
* Search for and add songs by title and artist
* Easily customize the song list and reuse the script for different themes

## Setup

1. Clone this repo:

   ```bash
   git clone https://github.com/thiebes/spotify-playlist-builder.git
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following:

   ```env
   CLIENT_ID=your_spotify_client_id
   CLIENT_SECRET=your_spotify_client_secret
   REDIRECT_URI=http://127.0.0.1:8888/callback
   ```

5. Run the script:

   ```bash
   python main.py
   ```

## Example

```python
track_list = [
    ("Alright", "Kendrick Lamar"),
    ("Freedom", "Beyoncé")
]
```

## License

MIT License — free to use, modify, and share.