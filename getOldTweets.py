#!/usr/bin/env python3

# Elisabetta Caldesi, Abe Leon, Leigh Campbell
# Social Sensing Project: Predicting Spotify's Next Top Hits
# Get old tweets about the songs of the training set to complete
# our regression model

# pip install -e git+https://github.com/Mottl/GetOldTweets3#egg=GetOldTweets3
# pip install cookiejar

import sys
import got
import codecs
from langdetect import detect
import time
from sentiments import clean_tweet, get_tweet_sentiment
from regex import filter_tweet
import json
import math

# open file containing songs for Training Set
trainingSet = codecs.open('NMF424_1.txt', encoding='utf-8', mode='r')
final_dict = {} # {1: {name: , id: , sentiment: , number: , time: , favorites: , rts: }, 2: {...}, ....}
song_num = 1

for song in trainingSet:
    print(song)
    song_dict = {} # dictionary for each song {name: , id: , sentiment: , number: , time: , favorites: , rts: }
    song = song.strip()
    song = song.split('^')
    title = song[0]
    artist = song[1]
    id = song[2]
    date = song[3]

    start_time = time.time() # time the search
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(title).setSince(date).setUntil("2019-04-24").setMaxTweets(4000)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    search_time = time.time() - start_time

    total_polarity = 0
    num_tweets = 0
    total_favorites = 0
    total_rts = 0

    # now analyze each tweet received about the individual song
    for t in tweets:
        favs = t.favorites
        rts = t.retweets
        try:
            # check that the tweet is in english
            if detect(t.text) == 'en':
                # filter the tweet
                filtered_t = filter_tweet(t.text, title, artist)
                if filtered_t != None:
                    # print filtered_t
                    num_tweets += 1
                    cleaned_t = clean_tweet(filtered_t)
                    polarity = get_tweet_sentiment(cleaned_t)
                    total_polarity += polarity
                    total_favorites += favs
                    total_rts += rts
        except:
            continue

    song_sentiment = total_polarity / float(num_tweets)
    # complete the song_dict with name, sentiment, number of tweets and time

    song_dict['name'] = title
    song_dict['id'] = id
    song_dict['sentiment'] = song_sentiment
    if (num_tweets == 0): num_tweets = 1
    if (search_time == 0): search_time = 0,01
    if (total_favorites == 0): total_favorites = 1
    if (total_rts == 0): total_rts = 1
    song_dict['log_number'] = math.log(num_tweets,10)
    song_dict['log_time'] = math.log(search_time,10)
    song_dict['log_favorites'] = math.log(total_favorites,10)
    song_dict['log_rts'] = math.log(total_rts,10)

    # now add the song_dict to the general dict
    final_dict[song_num] = song_dict
    song_num += 1


# now output final_dict on a json file
with open('NMF424_1.json', 'w') as outfile:
    json.dump(final_dict, outfile)
