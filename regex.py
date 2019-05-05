#!/usr/bin/env python3

# Elisabetta Caldesi
# Social Sensing Project
# STEP 3: Filter general tweets about each song with the use of regex

import re

def filter_tweet(tweet, track, author):
    tweet = tweet.lower()
    author = author.lower()
    author = author.split(',')
    track = track.lower()
    track = track.replace(',', '')

    p1 = '.*' + author[0] + '.*' + track + '.*' # Pattern1: '.*Ariana Grande.*God is a woman.*' -> main author + track
    p3 = '.*' + track + '.*' + author[0] + '.*'  # Pattern3: '.*God is a woman.*Ariana Grande.*' -> track + main author
    p2 = '.*' + track + '.*' # Pattern2: '.*God is a woman.*' -> only track
    
    # check for matches
    if ((re.search(p1, tweet) != None) or (re.search(p2, tweet) != None) or (re.search(p3, tweet) != None)):
        return tweet
    else:
        return None
