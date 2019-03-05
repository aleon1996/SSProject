#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:44:40 2019

@author: lcampbe3
"""

#two basic functions to clean and get the sentiment values of tweets
#install textblob by pip install textblob & python -m textblob.dowload_corpora
from textblob import TextBlob
import re

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentifment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

