#!/usr/bin/python

__author__ = 'Max'

import praw

user_agent = ("TrialBot v0.1")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("arguingaboutnothing")

for submission in subreddit.get_new(limit = 5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
