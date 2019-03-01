#!/usr/bin/env python3
import spotipy
import sys
import pprint
import spotipy.util as util

import os
from json.decoder import JSONDecodeError

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need your username!")
    print("usage: python new_releases.py [username]")
    sys.exit()

scope = 'user-top-read'
# try:
token = util.prompt_for_user_token(username, scope)
# except (AttributeError, JSONDecodeError):
# os.remove(f".cache-{username}")
# token = util.prompt_for_user_token(username, scope)

if token:
    #spotify:user:spotify:playlist:37i9dQZF1DX4JAvHpjipBk
    sp = spotipy.Spotify(auth=token)
    username = "spotify"
    playlist = "37i9dQZF1DX4JAvHpjipBk"
    sp_playlist = sp.user_playlist_tracks(username, playlist_id=playlist)
    tracks = sp_playlist['items']
    track_artist = {}
    for playlist_element in range(0, len(tracks)):
        song = tracks[playlist_element]['track']['name']
        artists = []
        for i in range(0, len(tracks[playlist_element]['track']['artists'])):
            artists.append(tracks[playlist_element]['track']['artists'][i]['name'])
        track_artist[song] = artists

    for k,v in track_artist.items():
        print('Song: '+str(k)+ ' Artist: '+ ', '.join(v))
    # sp = spotipy.Spotify(auth=token)
    #
    # response = sp.new_releases()
    #
    # while response:
    #     albums = response['albums']
    #     for i, item in enumerate(albums['items']):
    #         print(albums['offset'] + i,item['name'])
    #
    #     if albums['next']:
    #         response = sp.next(albums)
    #     else:
    #         response = None
else:
    print("Can't get token for", username)
