#!/usr/bin/env python3

# Elisabetta Caldesi, Abe Leon, Leigh Campbell
# Social Sensing Project: Predicting Spotify's Next Top Hits
# Get Training Set of Songs from elisabettacaldesi's playlist on spotify
# to obtain a training set of songs to build our multiple linear regression model

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
    print("usage: python getTrainingSetSongs.py [username]")
    sys.exit()

scope = 'playlist-read-private'
token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)

if token:
    sp = spotipy.Spotify(auth=token)
    username = "elisabettacaldesi"
    playlist = "37i9dQZF1DX4JAvHpjipBk"
    # username = "lcampbe3-us"
    # playlist = "4ce68f4vDXuZzGrpK6bHrK"
    sp_playlist = sp.user_playlist_tracks(username, playlist_id=playlist)
    tracks = sp_playlist['items']
    track_artist = {}
    for playlist_element in range(0, len(tracks)):
        song = tracks[playlist_element]['track']['name']
        id = tracks[playlist_element]['track']['id']
        release = tracks[playlist_element]['track']['album']['release_date']

        artists = []
        for i in range(0, len(tracks[playlist_element]['track']['artists'])):
            artists.append(tracks[playlist_element]['track']['artists'][i]['name'])
        str1 = id + '^' + release
        artists.append(str1)
        #artists.append(id)
        track_artist[song] = artists

    f = codecs.open('trainingSet.txt', encoding='utf-8', mode='w')
    for k,v in track_artist.items():
        f.write(k)
        f.write('^')
        f.write(','.join(v[:-1]))
        f.write('^')
        f.write(v[-1])
        f.write('\n')
    f.close()
else:
    print("Can't get token for", username)
