#!/usr/bin/env python3

# Elisabetta Caldesi, Abe Leon, Leigh Campbell
# Social Sensing Project: Predicting Spotify's Next Top Hits
# Get old tweets regarding our songs in the training set to complete
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

# open file containing songs for Training Set
trainingSet = codecs.open('trainingSet.txt', encoding='utf-8', mode='r')
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
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(title).setSince(date).setUntil("2019-03-31").setMaxTweets(4000)
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
    song_dict['number'] = num_tweets
    song_dict['number_vs_time'] = num_tweets/float(search_time)
    song_dict['favorites'] = total_favorites
    song_dict['rts'] = total_rts

    # now add the song_dict to the general dict
    final_dict[song_num] = song_dict
    song_num += 1


# now output final_dict on a json file
with open('trainingSet.json', 'w') as outfile:
    json.dump(final_dict, outfile)
