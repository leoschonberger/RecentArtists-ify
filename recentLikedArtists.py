import datetime

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from xlwt import Workbook

LINE_LIMIT = 255
NUMBER_OF_ARTISTS = 100

scope = 'user-library-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
artists_list = []


def get_tracks(results):
    for item in results['items']:
        track = item['track']
        # print(track['artists'][0]['name'], track['name'])
        check_counted(track)


def check_counted(track):
    cur_track_art_name = track['artists'][0]['name']
    if cur_track_art_name in artists_list:
        pass
        # print('Already found')
    else:
        artists_list.append(cur_track_art_name)
        # print('New Artist Found!')


def get_data() -> artists_list:
    print('Retrieving Data...')
    results = sp.current_user_saved_tracks()
    get_tracks(results)

    while results['next']:
        results = sp.next(results)
        get_tracks(results)

    return artists_list


def create_sheet():
    wb = Workbook()
    s1 = wb.add_sheet('Recent Artists')
    data = get_data()

    print('Formatting Data...')
    for artist_i in range(set_range(artists_list)):
        s1.write(artist_i, 0, data[artist_i])

    print("Done!")
    wb.save(f'Top artists {create_timestamp()}.xls')


def create_timestamp() -> str:
    time = str(datetime.datetime.now())
    # time = time.replace(' ', '')
    time = time.replace(':', '-')
    return time


# TODO: xlwt has a backwards compatibility limitation of 256 rows per
#       column. Microsoft Dumb. Good thing we only need 100.
def set_range(artists_list: artists_list) -> int:
    if len(artists_list) < NUMBER_OF_ARTISTS:
        return len(artists_list)
    else:
        return NUMBER_OF_ARTISTS


# Make sure to set your ENV vars
if __name__ == '__main__':
    create_sheet()