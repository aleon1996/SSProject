#!/usr/bin/env python3

# Elisabetta Caldesi
# Social Sensing Final Project
# STEP 5: Get Popularity Value for each song from Spotify

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

track_auths = []
newMusicFridayFile = codecs.open('newMusicFriday.txt', encoding='utf-8', mode='r')
for line in newMusicFridayFile:
    line = line.strip()
    line = line.split('"') # line[0] = track name, line[1] = artist
    track_name = line[0]
    authors = ', '.join(line[1])

    scope = 'playlist-read-private' # probably change this
    token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)

    if token:
        sp = spotipy.Spotify(auth=token)
        # Change this to fit to track rather than playlist

        username = "spotify"
        playlist = "37i9dQZF1DX4JAvHpjipBk"
        sp_playlist = sp.user_playlist_tracks(username, playlist_id=playlist)
        tracks = sp_playlist['items']
        track_popularity = {}
        for playlist_element in range(0, len(tracks)):
            song = tracks[playlist_element]['track']['name']
            artists = []
            for i in range(0, len(tracks[playlist_element]['track']['artists'])):
                artists.append(tracks[playlist_element]['track']['artists'][i]['name'])
            track_artist[song] = artists

        f = codecs.open('groundTruth.txt', encoding='utf-8', mode='w')
        for k,v in track_popularity.items():
            f.write(k)
            f.write(',')
            f.write(v)
            f.write('\n')
        f.close()
    else:
        print("Can't get token for", username)
