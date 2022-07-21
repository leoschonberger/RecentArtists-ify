# RecentArtists-ify - Artist lists made simple
Gets 100 artists from the most recent songs added to your spotify library. A project inspired by a friend.

##***Features:***

 - Spotify O-Auth client authentication 
 - Spotify API calls 
 - Export as .xls

## Usage:
1. Go to (https://developer.spotify.com/dashboard/)
2. "**Create an app**"and name it something 
3. Click "**Edit Settings**"
4. Add any URL under the "**Redirect URIs**" section.
Anything will do. Just remember it for now.
5. Go into PyCharm and **Edit Configurations**, under the run menu in the upper right.
6. Click on Environment Variables and set the following names to values that are in the spotify app UI:
- SPOTIPY_CLIENT_ID
- SPOTIPY_CLIENT_SECRET
- SPOTIPY_REDIRECT_URI

7. Check that both packages have been installed (use pip)
8. You're done! Run that sucker.
