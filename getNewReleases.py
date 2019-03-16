#!/usr/bin/env python3
import spotipy
import sys
import pprint
import spotipy.util as util
import codecs
import os

#from json.decoder import JSONDecodeError

SPOTIPY_CLIENT_ID='5b8dbcb9ff8f4fbcb3e62f0ae1f0b138'
SPOTIPY_CLIENT_SECRET=''
SPOTIPY_REDIRECT_URI='http://0.0.0.0:8000/' # run: python3 -m http.server 8000

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need your username!")
    print("usage: python getNewReleases.py [username]")
    sys.exit()

scope = 'playlist-read-private'
token = util.prompt_for_user_token(username,scope,client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI)
# except (AttributeError, JSONDecodeError):
# os.remove(f".cache-{username}")
# token = util.prompt_for_user_token(username, scope)

if token:
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

    f = codecs.open('newMusicFriday.txt', encoding='utf-8', mode='w')
    for k,v in track_artist.items():
        print('Song: '+str(k)+ ' Artist: '+ ', '.join(v))
        f.write(k)
        f.write('"')
        f.write(', '.join(v))
        f.write('\n')
    f.close()
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
