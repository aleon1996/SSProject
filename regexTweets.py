#!/usr/bin/env python3

# Elisabetta Caldesi
# Social Sensing Project
# STEP 3: Filter general tweets about each song with the use of regex

import codecs
import tweepy
import sys
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import re

# Find out number of songs in newMusicFriday.txt so that we open the right amount of files
num_songs = popen('cat newMusicFriday.txt | wc -l')
num_songs = int(num_songs) -1 # -1 if the last end of line is counted, just a matter of testing

# open file newMusicFriday.txt and save content in a list of lists called track_auths
newMusicFridayFile = codecs.open('newMusicFriday.txt', 'r', encoding="utf-8")
track_auths = [] # list of lists -> [[track1, 'author1, author2'], [track2, 'auth1, auth2']]
for line in newMusicFridayFile:
    line = line.strip()
    line = line.split('"')
    track_auths.append(line)

# create num_songs (90-100) files that contain the regex'ed tweets
for i in range(1, num_songs):
    read_from = 'dir_gen/tweets' + str(i) + '.txt' # open general tweets for each song -> dir_gen/tweets1.txt
    write_to = 'dir_regex/rxtweets' + str(i) + '.txt' # open file to write regex'ed tweets to -> dir_regex/rxtweets1.txt
    fread = codecs.open(read_from, 'r', encoding="utf-8")
    fwrite = codecs.open(write_to, 'w+', encoding="utf-8")
    # iterate through each tweet in the file
    for tweet in fread:
        tweet = tweet.strip()
        author = ', '.join(track_auths[i-1][1])
        author_upper = toupper(author)
        author_lower = tolower(author)
        track = track_auths[i-1][0]
        track_upper = toupper(track)
        track_lower = tolower(track)

        # Pattern1: '.*Ariana Grande.*God is a woman.*' -> author + track
        p1 = '.*' + author + track + '.*'
        p1lower = '.*' + author_lower + track_lower + '.*'
        p1upper = '.*' + author_upper + track_upper + '.*'
        p1combo1 = '.*' + author_lower + track_upper + '.*' # combinations
        p1combo2 = '.*' + author_upper + track_lower + '.*' #combinations

        # Pattern2: '.*God is a woman.*' -> track
        p2 = '.*' + track + '.*'
        p2lower = '.*' + track_lower + '.*'
        p2upper = '.*' + track_upper + '.*'

        # Pattern3: '.*God is a woman.*Ariana Grande.*' -> track + author
        p3 = '.*' + track + author + '.*'
        p3lower = '.*' + track_lower + author_lower + '.*'
        p3upper = '.*' + track_upper + author_upper + '.*'
        p3combo1 = '.*' + track_lower + author_upper + '.*' # combinations
        p3combo2 = '.*' + track_upper + author_lower + '.*' #combinations

        if ((re.search(p1, tweet) != 'None') or (re.search(p1lower, tweet) != 'None') or (re.search(p1upper, tweet) != 'None')
        or (re.search(p1combo1, tweet) != 'None') or (re.search(p1combo2, tweet) != 'None') or
        (re.search(p2, tweet) != 'None') or (re.search(p2lower, tweet) != 'None') or (re.search(p2upper, tweet) != 'None')
        or (re.search(p3, tweet) != 'None') or (re.search(p3lower, tweet) != 'None') or (re.search(p3upper, tweet) != 'None')
        or (re.search(p3combo1, tweet) != 'None') or (re.search(p3combo2, tweet) != 'None')):
            fwrite.write(tweet + '\n')
    fread.close()
    fwrite.close()
