import json

import requests
import praw

with open('./credentials.json') as f:
    params = json.load(f)

reddit = praw.Reddit(client_id=params['client_id'], 
                     client_secret=params['api_key'],
                     password=params['password'], 
                     user_agent='Getting posts for nlp analysis accessAPI:v0.0.1 (by /u/bathtub_physicist)',
                     username=params['username'])


subreddit = reddit.subreddit('loveconfession')
print(subreddit.display_name)
print(subreddit.title)  
print(subreddit.description)

posts_dict = {"posts": []} # [{"title": , "url": , "selftext": }]

for submission in subreddit.hot(limit=40):
    posts_dict["posts"].append({
        "title": submission.title,
        "url": submission.url,
        "selftext": submission.selftext
    })

with open('posts.json', 'w') as f:
    json.dump(posts_dict, f)
    print("Saved posts to file")