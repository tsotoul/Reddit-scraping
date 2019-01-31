#!/usr/bin/env python
# coding: utf-8

# Import the necessary libraries
import praw
import numpy as np
import pandas as pd

# Authenticate PRAW
reddit = praw.Reddit(client_id='xxxxxx',                     
                     client_secret='xxxxxx',                     
                     user_agent='data-wrangling-app')

#reddit.read_only (only used to check if authentication was successful)

# Get the posts for the wanted category/subreddit (music) and create a list to store them (posts)
category = 'music'
posts =  list(reddit.subreddit(category).top(limit=100))

#vars(posts[0]) (Only used to identify the required attributes)

# Initialise empty lists for the attribute data and the counters
score = []
above_100 = 0
comments = []
gilded = []
gilded_num = 0

# Loop through the posts and append the data to the relevant lists and counters
for item in posts:
    score.append(item.score)
    comments.append(item.num_comments)
    gilded.append(item.gilded)
    if item.score > 100: above_100 += 1
    if item.gilded != 0: gilded_num += 1
        
# Print the required results
print('1: The average score of the first 100 posts of the subreddit {} is {}.'.format(category, int(np.mean(score))))
print('2: {}% of the first 100 posts of the subreddit {} has score more than 100.'.format(above_100, category))
print('3: The first 100 posts of the subreddit {} have an average of {} comments.'.format(category, int(np.mean(comments))))
print('4: {}% of the first 100 posts of the subreddit {} were gilded.'.format(gilded_num, category))

