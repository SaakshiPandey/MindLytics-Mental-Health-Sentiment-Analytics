import praw
import streamlit as st

def fetch_posts(client_id, client_secret, user_agent, subreddit_name="depression", limit=5):
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for post in subreddit.hot(limit=limit):
        posts.append({
            "title": post.title,
            "content": post.selftext,
            "created": post.created_utc
        })
    return posts

def fetch_user_posts(client_id, client_secret, user_agent, username, limit=10):
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )
    user = reddit.redditor(username)
    posts = []

    for post in user.submissions.new(limit=limit):
        posts.append({
            "title": post.title,
            "content": post.selftext,
            "created": post.created_utc
        })

    return posts
