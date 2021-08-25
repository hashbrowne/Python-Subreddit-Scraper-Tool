import praw
import pandas as pd

reddit = praw.Reddit(client_id='client id', \
                     client_secret='client secret', \
                     user_agent='user agent', \
                     username='your reddit username', \
                     password='your reddit password')
posts = []
subreddit = reddit.subreddit('python')
for post in subreddit.top(limit=20):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id','subreddit','url','num_comments', 'body', 'created'])
print(posts)

posts.to_csv('C:\\Users\\You\\Desktop\\posts.csv')
