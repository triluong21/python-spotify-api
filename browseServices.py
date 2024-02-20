from dotenv import load_dotenv
import os
from requests import get
import json
from buildSecrets import getToken, getAuthHeader

load_dotenv()

spotify_url = os.getenv("SPOTIFY_URL")

def searchAlbumList(artist_name):
    token = getToken()
    headers = getAuthHeader(token)
    searchUrl = f"{spotify_url}search?q={artist_name}&type=artist&limit=1"
    result = get(searchUrl, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        return None
    
    album_id = json_result[0]["id"]
    
    searchAlbumUrl = f"{spotify_url}artists/{album_id}/top-tracks?country=US"
    result = get(searchAlbumUrl, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    albumList = []

    for i in range(len(json_result)):
        songTuple = (i + 1, json_result[i]["name"], json_result[i]["external_urls"]["spotify"])
        albumList.append(songTuple)


    return albumList
