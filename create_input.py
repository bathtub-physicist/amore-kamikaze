import json

import demoji

with open("./posts.json") as f:
    posts = json.load(f)

posts = posts["posts"]

compiled_text = []

for post in posts:
    text = demoji.replace(post["selftext"]).strip()
    compiled_text.append(text)

compiled_text = "\n\n".join(compiled_text).strip()

with open("input.txt", "w", encoding="utf-8") as f:
    f.write(compiled_text)