from ytmusicapi import YTMusic

import json
import requests
import functools

headers = open('./headers', 'r').read()
artists = [ l.strip('\n') for l in open('./artists.txt', 'r').readlines() ]

json = YTMusic.setup(filepath="headers_auth.json", headers_raw=headers)
ytmusic = YTMusic(json)

artist_ids = [
    ytmusic.search(query=a, filter='artists')[0]['browseId'] for a in artists
]

ytmusic.subscribe_artists(artist_ids)
