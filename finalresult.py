#!/usr/bin/env python3
import os
import sys
import time
import csv
import json
import tweepy
from sentiments import clean_tweet, get_tweet_sentiment
from regex import filter_tweet

with open('data.json', 'r') as f:
    d = json.load(f)
s = sum(d['1']['sentiment'])/len(d['1']['sentiment'])
print(s*100)
