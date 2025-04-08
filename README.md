# spotifile

For years, I had collected over 2,500 music videos stored locally — a mix of official tracks, fan edits, anime OSTs, retro songs, Nepali music, and random YouTube rips. It was chaotic, nostalgic, and totally unstreamable.

🎯 I wanted to breathe life into that archive — to turn it into a real, shareable, modern Spotify playlist.

So I built a full automation pipeline that:

🧼 Cleans and extracts song names from messy file titles like:

Queen - Bohemian Rhapsody (Official Video)(240P)

Imagine*Dragons*-\_Demons_low

Ghost Riders In The Sky Johnny Cash Full Song

🎶 Searches for each song on Spotify using full-text matching — with smart error handling and retry logic for unstable networks.

✅ Automatically creates a Spotify playlist with all valid songs.

📝 Logs missing or unmatched songs for review.

💡 All it needs is a .txt file of cleaned song titles — just drop it in, run the script, and your playlist builds itself.

🧠 How the Code Works
It scans a folder of videos and cleans the titles using regular expressions, removing things like [Lyrics], (240P), low, HD, etc.

Then it reads a cleaned titles.txt, sorts it alphabetically, and searches each entry using Spotify's API.

If the search fails due to timeout or network hiccups, it automatically retries before giving up.

Finally, it adds songs to a new playlist in batches of 100, respecting API limits, and saves not-found songs to a separate file for future cleanup or fuzzy matching.

What started as a cluttered archive of personal favorites turned into a curated digital legacy. I now have my old musical taste preserved and streamable — anywhere, anytime.

Every time I hit play, I’m reminded of my teenage years, my taste evolving, the obscure gems, the anime theme songs I looped, and those "unknown YouTube bangers" I never thought I’d hear again.

This wasn’t just about automation. It was about memory. It was about music.
