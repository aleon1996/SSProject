#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:48:05 2019

@author: lcampbe3
"""

import spotipy
import sys
import pprint
import spotipy.util as util
import codecs
import os

SPOTIPY_CLIENT_ID='5b8dbcb9ff8f4fbcb3e62f0ae1f0b138'
SPOTIPY_CLIENT_SECRET='04f0d2a4fdae4245ac26cdd496d65c05'
SPOTIPY_REDIRECT_URI='http://0.0.0.0:8000/' # run: python3 -m http.server 8000

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need your username!")
    print("usage: python getGroundTruths.py [username]")
    sys.exit()

newMusicFridayFile = codecs.open('trainingSet.txt', encoding='utf-8', mode='r')
f = codecs.open('trainingSetGroundTruth.txt', encoding='utf-8', mode='w')
for line in newMusicFridayFile:
    line = line.strip()
    line = line.split('^') # line[0] = track name, line[1] = artist, line[2] = track id
    track_name = line[0]
    authors = ','.join(line[1])
    track_id = line[2]

    scope = 'playlist-read-private'
    token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)

    if token:
        sp = spotipy.Spotify(auth=token)
        song = sp.track(track_id)

        f.write(song['name'])
        f.write('^')
        f.write(str(song['popularity']))
        f.write('^')
        f.write(str(track_id))
        f.write('\n')

f.close()
