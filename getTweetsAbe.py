#!/usr/bin/env python3
import os
import sys
import time
import csv
import json
import tweepy
from sentiments import clean_tweet, get_tweet_sentiment

CONSUMER_KEY = 'vHZIZtFTt5nNbSrPqlDAIJgNl'
CONSUMER_SECRET = 'ARrxyCHbCrUUh5NvVMJ8Z71RoxiGa3MaGZQAwQk7bDwE6Uua6I'
OAUTH_TOKEN = '408881182-wRq39dmJQsM4238wSi1rSJEMxtCDu7b99lPkRHUD'
OAUTH_TOKEN_SECRET = 'xz4ZCzHM3Vc3RQ2Qgq8zvh7c7UozPi67EnOgMYrg6r46h'

data = {} #this will be the dictionary holding all our tweet data

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
song_id = 1

api = tweepy.API(auth)
class StreamListenerKeywords(tweepy.StreamListener):

    def __init__(self, api=None):
        super(StreamListenerKeywords, self).__init__()
        self.num_tweets = 0
        self.start_time = time.time()
        # print("start time: {}".format(self.start_time))
        self.end_time = None
        self.final_time = None
        global song_id

    def on_status(self, status):
        tweet = clean_tweet(status.text)
        print(tweet)
        data[song_id]['tweets'].append(tweet)
        self.end_time = time.time()
        # print("end time: {}".format(self.end_time))
        self.final_time = self.end_time - self.start_time
        # print("time difference: {}".format(self.final_time))
        self.num_tweets += 1
        #we can change the ending of the stream based on a timer or number of tweets
        if self.final_time > 60:
            print("Time Limit Reached")
            data[song_id]['time'] = self.final_time
            return False

    def on_error(self, status_code):
        if status_code == 420:
            return False

def beginStream(line):
    stream_listener_keywords = StreamListenerKeywords()
    stream1 = tweepy.Stream(auth=api.auth, listener=stream_listener_keywords)
    stream1.filter(track=line , languages=['en'])

def main():
    #Read in File with New Music
    if len(sys.argv) != 2:
        print('Error, usage: ./getTweetsAbe newMusicFriday.txt')
        sys.exit()
    else:
        #Open file with song names and artist
        file_name = sys.argv[1]
        global song_id
        for line in open(file_name):
            line = line.rstrip()
            line = line.split('"') #line is a list of ['song', 'authors'] <-- could improve how to split authors
            #TODO we need better keywords, so if we could pass in regexTweets function to do that here that takes a list and returns a list that'd be ideal
            data[song_id]={}
            data[song_id]['name'] = line[0]
            data[song_id]['artist'] = line[1]
            data[song_id]['tweets'] = []
            data[song_id]['time'] = None
            #beginStream will collect X number of tweets per song, keeping in mind how long it takes to collect each for each song.
            #The less time it takes, we know the more this song is being talked about. Alternatively we also use a timer, up to us to decide
            beginStream(line)
            song_id+=1
        #write to json file once all tweets have been collectedself.
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

main()
