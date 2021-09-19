import requests
import sys

CLIENT_ID = '144a153dcf2b4d29bf48ec5b610942e2'
CLIENT_SECRET = 'c18582449e0b4e3ca732f8f45de5ba91'
AUTH_URL = 'https://accounts.spotify.com/api/token'
command = { 'grant_type': 'client_credentials', 'client_id': CLIENT_ID, 'client_secret': CLIENT_SECRET,}
auth_response = requests.post(AUTH_URL, data=command)

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
BASE_URL = 'https://api.spotify.com/v1/'
#artist_id = '36QJpDe2go2KgaRleHCDTp'
#params={'include_groups': 'album', 'limit': 50}
#r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums',  headers=headers, params=params)
#d = r.json()
#for album in d['items']:
#    print(album['name'], ' --- ', album['release_date'])

artist_id= str(sys.argv[1])
params={'limit': 50}
r = requests.get(BASE_URL + 'search?type=track&q=artist:' + artist_id, params=params, headers=headers)
d = r.json()['tracks']
for track in d['items']:
    print(track['name'] , '\t\t', track['popularity'], '\t\t' , track['album']['name'], '\t\t', track['album']['release_date'])		#track['uri']
