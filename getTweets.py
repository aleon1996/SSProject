#!/usr/bin/env python3

# Elisabetta Caldesi, Abe Leon, Leigh Campbell
# Social Sensing Project
# Twitter Crawler

import codecs
import tweepy
import sys
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler

# Twitter crawler Authorization tokens
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# create OAuth Handler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# build class Stream Listener to fetch tweets
class TweetListener(StreamListener):
    def __init__(self, api=None):
        super(TweetListener,self).__init__()
        self.max = 0

    def on_data(self, data):
        f = codecs.open('tweets.txt', 'w', encoding="utf-8")
        json_load = json.loads(data)
        text = {'text': json_load['text']}
        print json.dumps(text)
        #f.write(json.dumps(text) + '\n')
        self.max += 1
        if self.max > 49:
            f.close()
            sys.exit(0)
        return True

    def on_error(self, status):
        print status

# Read in Tracks and Artists from text file "newMusicFriday.txt"
# f = codecs.open('newMusicFriday.txt', encoding='utf-8', mode='r')
# for line in f:
#     line = line.strip()
#     line = line.split('"')

api = tweepy.API(auth)
twitterStream = Stream(auth=api.auth,listener=TweetListener())
twitterStream.filter(track=['God is a woman by Ariana Grande'], languages=['en'])
