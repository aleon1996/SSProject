#!/usr/bin/env python3

# Elisabetta Caldesi
# Social Sensing Project
# Search API instead of Streaming

import os
import sys
import time
import csv
import json
import tweepy
from sentiments import clean_tweet, get_tweet_sentiment
from regex import filter_tweet

global song_id
global song_name
global artists

consumer_key = "Nu4CkxEjjjadnSd46m7VqbGoI"
consumer_secret = "j7KKj24ZymLd14wrTWcL3Aae84LLWIqfH7mxfVDezoX4G7Lnti"
access_token = "1088148936190251010-SUMm6eJUponmQOv0iJBlg9vIRDchcb"
access_token_secret = "tDsEPByqsNJ1P3iRUVJIB7c3vXuMgA9ug1KCvVQBhAXHc"


data = {} #this will be the dictionary holding all our tweet data
song_name = None
artists = None

# create OAuth Handler instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

song_id = 1

# class StreamListenerKeywords(tweepy.StreamListener):
#
#     def __init__(self, api=None):
#         super(StreamListenerKeywords, self).__init__()
#         self.num_tweets = 0
#         self.start_time = time.time()
#         # print("start time: {}".format(self.start_time))
#         self.end_time = None
#         self.final_time = None
#
#     def on_status(self, status):
#
#         tweet = clean_tweet(status.text)
#         print("----------" + tweet + "----------->")
#         result = filter_tweet(tweet, song_name, artists)
#         if (result != None):
#             print(result)
#             polarity = get_tweet_sentiment(result)
#             print(polarity)
#             data[song_id]['sentiment'].append(polarity)
#             data[song_id]['tweets'].append(result)
#             self.num_tweets += 1
#
#         self.end_time = time.time()
#         # print("end time: {}".format(self.end_time))
#         self.final_time = self.end_time - self.start_time
#         # print("time difference: {}".format(self.final_time))
#         #we can change the ending of the stream based on a timer or number of tweets
#         if self.num_tweets > 20:
#             print("Time Limit Reached")
#             data[song_id]['time'] = self.final_time
#             data[song_id]["number"] = len(data[song_id]['tweets'])
#             return False
#
#     def on_error(self, status_code):
#         if status_code == 420:
#             return False

def beginSearch(line):

    # stream_listener_keywords = StreamListenerKeywords()
    # stream1 = tweepy.Stream(auth=api.auth, listener=stream_listener_keywords)

    auths = line[1].split(',')
    str1 = line[0] + ' '+ line[1].replace(',' , ' ')
    kw = [] # kw = ['song title', 'artist1', 'artist2', 'song title + all of the artists without commas']
    kw.append(line[0]) # kw = ['song title']
    kw += auths # kw = ['song title', 'artist1', 'artist2']
    kw.append(str1)
    print(kw)
    count = 1
    for tweet in tweepy.Cursor(api.search, q=kw, lang="en").items():
        if count < 100:
            print (tweet.text)
            count += 1

def main():
    #Read in File with New Music
    if len(sys.argv) != 2:
        print('Error, usage: ./getTweetsAbe [test file]')
        sys.exit()
    else:
        #Open file with song names and artist
        file_name = sys.argv[1]
        global song_id
        for line in open(file_name):
            global song_name
            global artists
            line = line.rstrip()
            line = line.split('"') #line is a list of ['song', 'authors''id'] <-- could improve how to split authors
            #TODO we need better keywords, so if we could pass in regexTweets function to do that here that takes a list and returns a list that'd be ideal
            data[song_id]={}
            song_name = line[0]
            artists = line[1]
            data[song_id]['name'] = line[0]
            data[song_id]['artist'] = line[1]
            data[song_id]['id'] = line[2]
            data[song_id]['tweets'] = []
            data[song_id]['time'] = None
            data[song_id]['sentiment'] = []
            #beginStream will collect X number of tweets per song, keeping in mind how long it takes to collect each for each song.
            #The less time it takes, we know the more this song is being talked about. Alternatively we also use a timer, up to us to decide
            beginSearch(line)
            song_id+=1
        # #write to json file once all tweets have been collectedself.
        # with open('data.json', 'w') as outfile:
        #     json.dump(data, outfile)

main()
