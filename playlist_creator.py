import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#loadind scraped pre-cleaned song titles or your titles
with open('YOUR TITLES TEXT FILE.txt', 'r', encoding='utf-8') as file:
    song_titles = [line.strip() for line in file if line.strip()]

song_titles.sort()


# authenticationg spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    client_id = "YOUR CLIENT ID",
    client_secret = "YOUR SECRET CODE",
    redirect_uri="http://localhost:8888/callback",
    show_dialog=True,
    cache_path="token.txt"
))
user_id = sp.current_user()["id"]

# creating a playlist
playlist_name = "NAME FOR YOUR PLAYLIST IN SPOTIFY"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
print(f"🎵 Created playlist: {playlist['name']}")

song_uris = []
not_found = []
seen_titles = set()

#search and collect
for index, song in enumerate(song_titles, 1):
    if song.lower() in seen_titles:
        continue
    seen_titles.add(song.lower())

    print(f"[{index}/{len(song_titles)}] 🔍 Searching for: {song}")
    try:
        result = sp.search(q=song, type="track", limit=1)
        tracks = result.get("tracks", {}).get("items", [])

        if tracks:
            uri = tracks[0]["uri"]
            song_uris.append(uri)
            print(f"   ✅ Found and added: {song}")
        else:
            print(f"   ❌ Not found: {song}")
            not_found.append(song)
    except Exception as e:
        print(f"   ⚠️ Error: {song} → {e}")
        not_found.append(song)

# add songs to playlist by making branches of 100
if song_uris:
    print(f"\n🎯 Adding {len(song_uris)} songs to playlist in batches...")
    for i in range(0, len(song_uris), 100):
        batch = song_uris[i:i+100]
        sp.playlist_add_items(playlist_id=playlist["id"], items=batch)
        print(f"   ➕ Added batch {i//100 + 1} ({len(batch)} songs)")

    print(f"\n✅ Finished adding songs to playlist: {playlist['external_urls']['spotify']}")
else:
    print("❌ No songs found to add.")

# saving songs that are not found in spotify
if not_found:
    with open('not_found.txt', 'w', encoding='utf-8') as f:
        for nf in not_found:
            f.write(nf + '\n')
    print(f"⚠️ Saved {len(not_found)} missing titles to 'not_found.txt'")
else:
    print("✅ All songs were found and added.")
