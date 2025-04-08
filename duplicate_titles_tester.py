with open('scraped_titles.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip().lower() for line in f if line.strip()]

total = len(lines)
unique = len(set(lines))
print(f"Total: {total}, Unique: {unique}, Duplicates: {total - unique}")
# add your file and sort the duplicates for aussarance playlist_creator removes duplicate automatically 
# so this is not necessary