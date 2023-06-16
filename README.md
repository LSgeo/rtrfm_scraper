# rtrfm_scraper

I <3 RTRFM!
https://rtrfm.com.au/

[RTRFM is](https://rtrfm.com.au/who-we-are/) a Perth community supported radio with a wide range of shows, airing and streaming from Boorloo (Perth) Western Australia.

Shows can be restreamed for up to one month after they air, in glorious 64 kbps.
For anyone with a spotify account, this app creates a playlist of all the tracks selected by the Show Presenter.

It **does**:
- Looks at the artist - track information entered by the RTRFM presenter
- Searches Spotify for the 1st search result
- Adds it to a new playlist on your authenticated Spotify account
- This uses Spotify OAuth, meaning the app cannot see your password, and its permissions are defined in the code

It **does not**L
- Find all tracks all the time
- Find the correct tracks all the time
- Include the advertisments and presenter notes from the broadcast :'(

Listen to the Restream first! Otherwise:
- You will miss out on the broadcast!
- You will miss out on hearing your favourite presenter!
- You will also miss: The gig guide, supporting your local RTRFM sponsors, etc.

I firmly encourage you to first listen to the restream on RTRFM, then turn to the playlist.


Usage:
- Sign up to Spotify Developer API access
- Create a file with the required tokens, to be imported and used in the app
- Then run the script, with the show to scrape as the first and only argument
