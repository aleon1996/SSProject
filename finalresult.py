#!/usr/bin/env python3
import os
import sys
import time
import csv
import json
import tweepy

with open('data.json', 'r') as f:
    d = json.load(f)
s = sum(d['1']['sentiment'])/len(d['1']['sentiment'])
number = d['1']['number']
time = d['1']['time']
print(s*100)
print(number)
print(time)
