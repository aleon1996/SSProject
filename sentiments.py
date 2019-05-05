#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:44:40 2019

@author: lcampbe3
"""

#two basic functions to clean and get the sentiment values of tweets
#install textblob by pip install textblob & python -m textblob.dowload_corpora OR python -m pip install -U textblob if link between python breaks
from textblob import TextBlob
import re

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    # print(analysis.sentiment.polarity)
    if analysis.sentiment.polarity > 0:
        #print('positive')
        return analysis.sentiment.polarity
    elif analysis.sentiment.polarity == 0:
        #print('neutral')
        return analysis.sentiment.polarity
    else:
        #print('negative')
        return analysis.sentiment.polarity
