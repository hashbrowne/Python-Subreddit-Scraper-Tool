import praw
import pandas as pd

reddit = praw.Reddit(client_id='yJABSToQgLAqy1znCKtV6A', \
                     client_secret='5FPPr7TZWt6eJeeZDh-Vv_qOgaMiNg', \
                     user_agent='Scraper', \
                     username='garbansko', \
                     password='walker75')
posts = []
subreddit = reddit.subreddit('python')
for post in subreddit.top(limit=15):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
print(posts)
