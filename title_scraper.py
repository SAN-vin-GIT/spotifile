import os
import re

folder_path = r'YOUR FOLDER'

video_extensions = ('.mp4', '.mkv', '.avi', '.mov', '.webm')

import re

import re

def clean_title(raw_title):
    #  to lowercase
    title = raw_title.lower()

    # removes resolution/quality metadata
    title = re.sub(r'\(?\d{3,4}[pP]\)?', '', title)
    title = re.sub(r'\(\s*\d+\s*[xX]\s*\d+\s*\)', '', title)

    # removes bracketed or piped expressions
    title = re.sub(r'[\[\(\|].*?[\]\)\|]', '', title)

    # replace common separators with space
    title = re.sub(r'[_\-\.]', ' ', title)

    # remove extra non-letter characters (keep spaces)
    title = re.sub(r'[^a-z\s]', '', title)

    # collapse multiple spaces
    title = re.sub(r'\s+', ' ', title).strip()

    # add junk words/phrases to remove
    garbage_words = {
        'official', 'video', 'lyrics', 'lyric', 'cover', 'remastered', 'remaster',
        'live', 'audio', 'youtube', 'low', 'high', 'hq', 'hd', 'feat', 'ft',
        'version', 'extended', 'ost', 'theme', 'soundtrack', 'visualizer', 'reaction',
        'edit', 'trailer', 'intro', 'outro', 'music', 'track', 'fanmade', 'mv', 'full', 'song'
    }

    # remove unwanted words from final list
    words = title.split()
    cleaned_words = [word for word in words if word not in garbage_words]

    # returts cleaned and capitalized
    return ' '.join(cleaned_words).title()

    # turns lowercase for matching
    title = raw_title.lower()

    # remove resolution/quality tags
    title = re.sub(r'\(?\d{3,4}[pP]\)?', '', title)
    title = re.sub(r'\(\s*\d+\s*[xX]\s*\d+\s*\)', '', title)

    # remove anything in [], (), or || — tag-like garbage
    title = re.sub(r'[\[\(\|].*?[\]\)\|]', '', title)

    # removes known junk words/phrases no matter where they are
    garbage_words = [
        r'official( music)? video', r'full song', r'lyrics?', r'cover', r'remaster(ed)?',
        r'live', r'audio', r'youtube', r'high', r'low', r'hq', r'hd', r'feat\.?', r'ft\.?',
        r'extended', r'ost', r'theme', r'soundtrack', r'visualizer', r'reaction', r'edit',
        r'trailer', r'intro', r'outro', r'music', r'track', r'fanmade', r'mv'
    ]
    for word in garbage_words:
        title = re.sub(r'\b' + word + r'\b', '', title)

    # replace underscores, hyphens, dots with space
    title = re.sub(r'[_\-\.]', ' ', title)

    # removes any non-letter characters except space
    title = re.sub(r'[^a-z\s]', '', title)

    # collapses multiple spaces
    title = re.sub(r'\s+', ' ', title)

    return title.strip().title()  # Capitalize Each Word

    # removes file quality info like (240P), (360 x 640), etc
    title = re.sub(r'\(?\d{3,4}[pP]\)?', '', raw_title)
    title = re.sub(r'\(\s*\d+\s*[xX]\s*\d+\s*\)', '', title)
    title = re.sub(
    r'(?i)\b(official|lyrics?|video|cover|remastered|remaster|live|audio|you[\s_]?tube|low|high|hq|hd|feat|full song|ft|version|extended|ost|theme|soundtrack)\b',
    '', title
)
    
    


    # removes common tag words and noise
    title = re.sub(
        r'(?i)\b(official|lyrics?|video|cover|remastered|remaster|live|audio|you[\s_]?tube|low|high|hq|hd|feat|ft|version|extended|ost|theme|soundtrack)\b',
        '', title
    )

    # removes anything in parentheses or brackets
    title = re.sub(r'[\[\(].*?[\]\)]', '', title)

    # removes underscores, hyphens, numbers, and extra symbols
    title = re.sub(r'[_\-\.]', ' ', title)
    title = re.sub(r'\d+', '', title)
    title = re.sub(r'[^a-zA-Z\s]', '', title)

    # collapses spaces
    title = re.sub(r'\s+', ' ', title).strip()

    return title





# cleaned titles are collected
titles = []
for file in os.listdir(folder_path):
    if file.lower().endswith(video_extensions):
        raw_title = os.path.splitext(file)[0]
        cleaned = clean_title(raw_title)
        if cleaned:
            titles.append(cleaned)

# save the titles to a file
with open('scraped_titles.txt', 'w', encoding='utf-8') as f:
    for title in titles:
        f.write(title + '\n')

print("✅ Clean titles saved to 'scraped_titles.txt'")
