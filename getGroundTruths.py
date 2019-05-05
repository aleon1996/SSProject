#!/usr/bin/env python3

# Elisabetta Caldesi, Abe Leon, Leigh Campbell
# Social Sensing Project: Predicting Spotify's Next Top Hits
# Retrieve the SPI's from Spotify to test the model

import spotipy
import sys
import pprint
import spotipy.util as util
import codecs
import os

# Insert API keys here
# SPOTIPY_CLIENT_ID=
# SPOTIPY_CLIENT_SECRET=
# SPOTIPY_REDIRECT_URI=
# run: python3 -m http.server 8000

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need your username!")
    print("usage: python getGroundTruths.py [username]")
    sys.exit()

newMusicFridayFile = codecs.open('NMF424_1.txt', encoding='utf-8', mode='r')
f = codecs.open('NMF424GroundTruth_1.txt', encoding='utf-8', mode='w')
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
