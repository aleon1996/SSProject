#!/usr/bin/env python3

# Elisabetta Caldesi
# Social Sensing Project
# STEP 2: Twitter Crawler to get general tweets about each song

import codecs
import tweepy
import sys
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import re

# Twitter crawler Authorization tokens
consumer_key = "Nu4CkxEjjjadnSd46m7VqbGoI"
consumer_secret = "j7KKj24ZymLd14wrTWcL3Aae84LLWIqfH7mxfVDezoX4G7Lnti"
access_token = "1088148936190251010-SUMm6eJUponmQOv0iJBlg9vIRDchcb"
access_token_secret = "tDsEPByqsNJ1P3iRUVJIB7c3vXuMgA9ug1KCvVQBhAXHc"

# create OAuth Handler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# build class Stream Listener to fetch tweets
class TweetListener(StreamListener):
    def __init__(self, api=None):
        super(TweetListener,self).__init__()
        self.max = 0
        self.file_num = 1   # NOT SURE THAT THIS IS GOING TO WORK, NEEDS TO BE TESTED

    def on_data(self, data):
        filename = 'dir_gen/tweets' + str(file_num) + '.txt' # create a new filename for each track
        f = codecs.open(filename, 'w+', encoding="utf-8")
        #f = codecs.open('tweets.txt', 'a', encoding="utf-8")
        json_load = json.loads(data)
        text = {'text': json_load['text']}
        print json.dumps(text)
        #f.write(json.dumps(text) + '\n')
        self.max += 1
        if self.max > 49: # set a higher number (should be 1500 before the rate limit)
            f.close()
            self.file_num += 1
            sys.exit(0)
        return True

    def on_error(self, status):
        print status

# Read in Tracks and Artists from text file "newMusicFriday.txt"
f = codecs.open('newMusicFriday.txt', encoding='utf-8', mode='r')
for line in f:
    line = line.strip()
    line = line.split('"')
    track = line[0]
    authors = ', '.join(line[1])

    twitterStream = Stream(auth=api.auth,listener=TweetListener())
    # WHAT SHOULD WE FILTER FOR??
    twitterStream.filter(track=['Ariana Grande God is a woman'], languages=['en'])
